class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head == None

    def enqueue(self, item):
        temp = Node(item)
        self.size += 1
        if self.head == None:
            self.head = self.tail = temp
        else:
            self.tail.set_next(temp)
            self.tail = temp

    def deque(self):
        if self.is_empty():
            return
        self.size -= 1
        temp = self.head.get_data()
        self.head = self.head.get_next()
        return temp

    def get_size(self):
        return self.size

    def print(self):
        current = self.head
        while current != None:
            print(current.get_data(), end=" ")
            current = current.get_next()
        print(" ")


if __name__ == "__main__":
    print("=" * 50)
    q = Queue()
    q.enqueue(50)
    q.enqueue(60)
    q.enqueue(70)
    print(q.is_empty())
    print(q.get_size())
    q.print()
    q.deque()
    print(q.get_size())
    q.print()
    q.deque()
    print(q.get_size())
    q.deque()
    print(q.get_size())
