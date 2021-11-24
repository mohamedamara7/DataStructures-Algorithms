class BinaryTree:
    def __init__(self, init_data):
        self.data = init_data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, new_data):
        self.data = new_data

    def insert_left(self, newNode):
        if self.left == None:  # don't have a left
            self.left = BinaryTree(newNode)
        else:  # if there is a left but this node between current node and the left
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp

    def insert_right(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp


if __name__ == "__main__":
    r = BinaryTree('a')
    r.insert_left('m')
    r.insert_right('o')
    print(r.get_left().get_data())
    print(r.get_right().get_data())
    r.get_right().set_data('K')
    print(r.get_right().get_data())
