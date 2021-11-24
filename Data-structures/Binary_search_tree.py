class Bstnode:
    def __init__(self, newkey, newval):
        self.key = newkey
        self.value = newval
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def bstsearch(self, subtree, target):
        if subtree is None:
            return None
        elif target > subtree.key:
            return self.bstsearch(subtree.right, target)
        elif target < subtree.key:
            return self.bstsearch(subtree.left, target)
        else:
            return subtree

    def has_key(self, target):
        return self.bstsearch(self.root, target) is not None

    def valueof(self, target):
        node = self.bstsearch(self.root, target)
        assert node is not None, "Invalid key"
        return node.value

    def bstminimum(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self.bstminimum(subtree.left)

    def bstmaximum(self, subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self.bstminimum(subtree.right)

    def add(self, newkey, newval):
        node = self.bstsearch(self.root, newkey)
        if node is not None:
            node.value = newval
            return False
        else:
            self.root = self.bstinsert(self.root, newkey, newval)
            self.size += 1
            return True

    def bstinsert(self, subtree, newkey, newval):
        if subtree is None:
            subtree = Bstnode(newkey, newval)
        elif newkey > subtree.key:
            subtree.right = self.bstinsert(subtree.right, newkey, newval)
        else:
            subtree.left = self.bstinsert(subtree.left, newkey, newval)
        return subtree

    def remove(self, key):
        node = self.bstsearch(self.root, key)
        assert node is not None, "Invalid key"
        self.root = self.bstremove(self.root, key)
        self.size -= 1

    def bstremove(self, subtree, key):
        if key > subtree.key:
            subtree.right = self.bstremove(subtree.right, key)
        elif key < subtree.key:
            subtree.left = self.bstremove(subtree.left, key)
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is not None and subtree.right is None:
                return subtree.left
            elif subtree.left is None and subtree.right is not None:
                return subtree.right
            else:
                successor = self.bstminimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self.bstremove(subtree.right, successor.key)
                return subtree
