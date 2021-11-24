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


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, item):
        temp = Node(item)
        temp.set_next(self.top)
        self.top = temp

    def peek(self):
        return self.top.get_data()

    def pop(self):
        temp = self.top.get_data()
        self.top = self.top.get_next()
        return temp

    def size(self):
        current = self.top
        cnt = 0
        while current is not None:
            cnt += 1
            current = current.get_next()
        return cnt

    def to_str(self):
        current = self.top
        res_str = ""
        while current != None:
            res_str += str(current.get_data())
            current = current.get_next()
        return res_str

if __name__ == "__main__":
    s = Stack()
    s.push(11)
    s.push(23)
    s.push(15)
    s.pop()
    print(s.size())
    print(s.peek())
    print(s.to_str())