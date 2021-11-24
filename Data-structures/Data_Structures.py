class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


########################################alternative method for stack#######################
class AStack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


###########################################################################################
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def deque(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


#############################################################################################
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorederedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        previous = None
        current = self.head
        while current != None:
            if current.get_data() == item:
                break
            previous = current
            current = current.get_next()
        if previous == None:
            self.head = self.head.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        temp = Node(item)
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(temp)

    def index(self, item):
        current = self.head
        idx = 0
        while current != None:
            if current.get_data() == item:
                return idx
            idx += 1
            current = current.get_next()

    def insert(self, pos, item):
        temp = Node(item)
        if pos == 0:
            temp.set_next(self.head)
            self.head = temp
            return
        current = self.head
        idx = 0
        while idx != pos - 1:
            idx += 1
            current = current.get_next()
        temp.set_next(current.get_next())
        current.set_next(temp)

    def pop(self, pos=None):
        if pos == None:
            current = self.head
            while current.get_next().get_next() != None:
                current = current.get_next()
            temp = current.get_next().get_data()
            current.set_next(None)
            return temp
        else:
            if pos == 0:
                temp = self.head.get_data()
                self.head = self.head.get_next()
                return temp
            idx = 0
            current = self.head
            while idx != pos - 1:
                idx += 1
                current = current.get_next()
            temp = current.get_next().get_data()
            current.set_next(current.get_next().get_next())
            return temp

    def print(self):
        current = self.head
        while current != None:
            print(current.get_data(), end=" ")
            current = current.get_next()
        print(" ")

    def get_head(self):
        return self.head


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        while current != None:
            if current.get_data() > item:
                break
            previous = current
            current = current.get_next()
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            if current.get_data() > item:
                return False
            current = current.get_next()
        return False

    def remove(self, item):
        previous = None
        current = self.head
        while current != None:
            if current.get_data() == item:
                break
            previous = current
            current = current.get_next()
        if previous == None:
            self.head = self.head.get_next()
        else:
            previous.set_next(current.get_next())

    def index(self, item):
        current = self.head
        idx = 0
        while current != None:
            if current.get_data() == item:
                return idx
            idx += 1
            current = current.get_next()

    def pop(self, pos=None):
        if pos == None:
            current = self.head
            while current.get_next().get_next() != None:
                current = current.get_next()
            temp = current.get_next().get_data()
            current.set_next(None)
            return temp
        else:
            if pos == 0:
                temp = self.head.get_data()
                self.head = self.head.get_next()
                return temp
            idx = 0
            current = self.head
            while idx != pos - 1:
                idx += 1
                current = current.get_next()
            temp = current.get_next().get_data()
            current.set_next(current.get_next().get_next())
            return temp

    def print(self):
        current = self.head
        while current != None:
            print(current.get_data(), end=" ")
            current = current.get_next()
        print(" ")


class UnorederedList_with_tail:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        temp = Node(item)
        if self.head == None:
            self.tail = temp
        temp.set_next(self.head)
        self.head = temp

    def append(self, item):
        temp = Node(item)
        temp.set_next(None)
        self.tail.set_next(temp)

    def print(self):
        current = self.head
        while current != None:
            print(current.get_data(), end=" ")
            current = current.get_next()
        print(" ")


if __name__ == "__main__":
    # print("Welcome to stack")
    # my_stack = Stack()
    # my_stack.push("hello")
    # my_stack.push("world")
    # print("size:", my_stack.size())
    # print(my_stack.peek())
    # print(my_stack.pop())
    # print(my_stack.pop())
    # print("isEmpty:", my_stack.isEmpty())
    # temp = Node(93)
    # var = 55
    # print(temp.get_data())
    # print(temp.get_next())
    # temp.set_data(22)
    # temp.set_next(var)
    # print(temp.get_data())
    # print(temp.get_next())
    # ul=UnorederedList()
    # ul.add(3)
    # ul.add(5)
    # ul.add(9)
    # ul.print()
    # print("**************************************")
    # ul.pop(1)
    # print(ul.index(6))
    # print("**************************************")
    # ul.print()
    # ul = UnorederedList_with_tail()
    # ul.add(3)
    # ul.add(5)
    # ul.add(9)
    # ul.print()
    # ul.append(222)
    # print("**************************************")
    # ul.print()
    ul = OrderedList()
    ul.add(5)
    ul.add(3)
    ul.add(18)
    ul.add(9)
    ul.print()
    print("**************************************")
    print(ul.search(1))
