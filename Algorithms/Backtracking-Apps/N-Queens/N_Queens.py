class Nqueens:
    def __init__(self, n):
        self.n = n
        self.numQueens = 0
        self.board = [['X' for i in range(n)] for j in range(n)]

    def len(self):
        return self.n

    def num_Queens(self):
        return self.numQueens

    def check_pos(self, r, c):
        # I am using backtracking algorithm so i don't need to check what after me, all i need is to check what behind me
        # So, we won't check the 8 directions only left side ,upper diagonal in left side and lower diagonal in left side

        # checking left side
        for i in range(c - 1, -1, -1):
            if self.board[r][i] == "Q":
                return False
        # checking upper diagonal in left side
        for i, j in zip(range(r - 1, -1, -1), range(c - 1, -1, -1)):
            if self.board[i][j] == "Q":
                return False
        # checking lower diagonal in left side
        for i, j in zip(range(r + 1, self.n, 1), range(c - 1, -1, -1)):
            if self.board[i][j] == "Q":
                return False
        return True

    def draw(self):
        for i in self.board:
            print(i)

    def solving(self, col=0):
        if col >= self.n:
            return True
        for i in range(self.n):
            if self.check_pos(i, col):
                self.board[i][col] = 'Q'
                if self.solving(col + 1):
                    return True
                self.board[i][col] = 'X'
        return False

    def final(self):
        if self.solving():
            self.draw()
        else:
            print("Can't")


if __name__ == "__main__":
    Q = Nqueens(8)
    Q.final()
