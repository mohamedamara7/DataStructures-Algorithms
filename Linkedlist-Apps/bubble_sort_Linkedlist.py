from random import randrange
from Data_Structures import UnorederedList


def random_values():
    linked_list = UnorederedList()
    for i in range(10000):
        linked_list.add(randrange(-1000, 1001))
    return linked_list


def bubble_sort_linkedlist(linked_list):
    n = linked_list.size() - 1
    for i in range(n, 0, -1):
        exchange = False
        current = linked_list.get_head()
        next = current.get_next()
        for j in range(i):
            if current.get_data() > next.get_data():
                temp = current.get_data()
                current.set_data(next.get_data())
                next.set_data(temp)
                exchange = True
            current = next
            next = next.get_next()
        if not exchange:
            break

linkedList = random_values()
linkedList.print()
print(linkedList.size())
bubble_sort_linkedlist(linkedList)
linkedList.print()
