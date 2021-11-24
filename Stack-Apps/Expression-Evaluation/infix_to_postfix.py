from pythonds import Stack


def infix_to_postfix(infix_exp):
    opStack = Stack()
    postfixlist = []
    tokenlist = infix_exp.split()
    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    for token in tokenlist:
        if token not in "^*/+-()":
            postfixlist.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ')':
            top_stack = opStack.pop()
            while top_stack != "(":
                postfixlist.append(top_stack)
                top_stack = opStack.pop()
        else:
            while (not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]):
                postfixlist.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixlist.append(opStack.pop())
    return " ".join(postfixlist)


if __name__ == "__main__":
    str = "a + b * c ^ d / e - f"
    str = infix_to_postfix(str)
    print(str)
    str = "120 + 35 * 31 ^ 2 / 13 - 5"
    str = infix_to_postfix(str)
    print(str)
