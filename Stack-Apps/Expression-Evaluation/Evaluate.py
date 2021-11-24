from pythonds import Stack


def do_math(operator, op1, op2):
    if operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    elif operator == "*":
        return op1 * op2
    elif operator == "/":
        return op1 / op2
    else:
        return op1 ** op2


def evaluation(postfix_exp):
    opStack = Stack()
    tokenlist = postfix_exp.split()
    for token in tokenlist:
        if token not in "^/*+-":
            opStack.push(int(token))
        else:
            op2 = opStack.pop()
            op1 = opStack.pop()
            opStack.push(do_math(token, op1, op2))
    return opStack.pop()


if __name__ == "__main__":
    str = "120 35 31 2 ^ * 13 / + 5 -"
    str = evaluation(str)
    print(str)
