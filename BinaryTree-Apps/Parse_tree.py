from pythonds import BinaryTree
from pythonds import Stack, Queue

import operator


def buildParseTree(fpexp):
    tokenlist = fpexp.split()
    ptree = BinaryTree('')
    curr = ptree
    pStack = Stack()
    pStack.push(ptree)
    for token in tokenlist:
        if token == '(':
            pStack.push(curr)
            curr.insert_left('')
            curr = curr.get_left()
        elif token in "+-*/^":
            pStack.push(curr)
            curr.set_data(token)
            curr.insert_right('')
            curr = curr.get_right()
        elif token == ')':
            curr = pStack.pop()
        else:
            curr.set_data(float(token))
            curr = pStack.pop()
    return ptree


def evaluate_ptree(ptree):
    opers = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul, '^': operator.pow}
    left_node = ptree.get_left()
    right_node = ptree.get_right()
    if left_node and right_node:
        fn = opers[ptree.get_data()]
        return fn(evaluate_ptree(left_node), evaluate_ptree(right_node))
    else:
        return ptree.get_data()


#########################################Depth First Search#########################################

def preorder_traversing(btree):
    if btree:
        print(btree.get_data(), end=" ")
        preorder_traversing(btree.get_left())
        preorder_traversing(btree.get_right())


def postorder_traversing(btree):
    if btree:
        postorder_traversing(btree.get_left())
        postorder_traversing(btree.get_right())
        print(btree.get_data(), end=" ")


def inorder_traversing(btree):
    if btree:
        inorder_traversing(btree.get_left())
        print(btree.get_data(), end=" ")
        inorder_traversing(btree.get_right())


#########################################Depth First Search#########################################
def level_order_traversing(btree):
    if btree == None:
        return
    q = Queue()
    q.enqueue(btree)
    while not q.isEmpty():
        currnode = q.dequeue()
        print(currnode.get_data(), end=" ")
        if currnode.get_left() != None:
            q.enqueue(currnode.get_left())
        if currnode.get_right() != None:
            q.enqueue(currnode.get_right())


if __name__ == "__main__":
    test_tree = buildParseTree("( ( ( 8 * ( 3 ^ 2 ) ) / 3 ) + 5 )")
    postorder_traversing(test_tree)
    print(end='\n')
    preorder_traversing(test_tree)
    print(end='\n')
    inorder_traversing(test_tree)
    print(end='\n')
    level_order_traversing(test_tree)
