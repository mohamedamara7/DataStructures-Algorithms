from pythonds.basic.stack import Stack


class Cellpos:
    def __init__(self, r, c):
        self.row = r
        self.col = c


class Maze:
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.items = [['.' for j in range(numCols)] for i in range(numRows)]
        self.start = None
        self.end = None

    def numRows(self):
        return self.numRows

    def numCols(self):
        return self.numCols

    def setWall(self, r, c):
        assert ((r < self.numRows and r >= 0) and (c < self.numCols and c >= 0)), "Out of range"
        self.items[r][c] = '*'

    def setStart(self, r, c):
        assert ((r < self.numRows and r >= 0) and (c < self.numCols and c >= 0)), "Out of range"
        self.start = Cellpos(r, c)

    def setEnd(self, r, c):
        assert ((r < self.numRows and r >= 0) and (c < self.numCols and c >= 0)), "Out of range"
        self.end = Cellpos(r, c)

    def draw(self):
        self.items[self.start.row][self.start.col] = 'S'
        self.items[self.end.row][self.end.col] = 'E'
        for i in self.items:
            print(i)

    def reset(self):
        for i in range(self.numCols):
            for j in range(self.numRows):
                if self.items[i][j] == "O":
                    self.items[i][j] = '.'

    def move(self, i, j):
        di = [-1, 1, 0, 0]
        dj = [0, 0, 1, -1]
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            if (new_i < 0 or new_i >= self.numRows or new_j < 0 or new_j >= self.numCols) or (
                    self.items[new_i][new_j] != '.'):
                continue
            self.items[new_i][new_j] = 'X'
            return new_i, new_j
        self.items[i][j] = 'O'
        return i, j

    def findPath_iteratively(self):
        S = Stack()
        i, j = (self.start.row, self.start.col)
        while self.items[self.start.row][self.start.col] != 'O':
            if self.items[i][j] == "O":
                (i, j) = S.pop()
            else:
                temp_i, temp_j = i, j
                temp_i, temp_j = self.move(i, j)
                if self.items[temp_i][temp_j] == "O":
                    S.pop()
                    continue
                if (temp_i, temp_j) == (self.end.row, self.end.col):
                    return True
                self.items[i][j] = 'X'
                i, j = temp_i, temp_j
                S.push((i, j))
        self.reset()
        return False

    def findPath_recuresion(self, r, c):
        if (r < 0 or c < 0 or r >= self.numRows or c >= self.numCols or self.items[r][c] != '.'):
            return False
        self.items[r][c] = "X"
        if (r, c) == (self.end.row, self.end.col):
            return True
        if self.items[self.start.row][self.start.col] == 'O':
            return False
        if (self.findPath_recuresion(r - 1, c) or self.findPath_recuresion(r + 1, c) or self.findPath_recuresion(r,
            c - 1) or self.findPath_recuresion(r, c + 1)):
            return True
        self.items[r][c] = "O"
        return False

    def Find(self):
        if self.findPath_recuresion(self.start.row, self.start.col):
            return True
        else:
            self.reset()
            return False
