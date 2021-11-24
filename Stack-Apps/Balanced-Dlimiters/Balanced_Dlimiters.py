from pythonds import Stack


def IsValidSource(src):
    s = Stack()
    for line in src:
        for token in line:
            if token in "({[":
                s.push(token)
            elif token in ")}]":
                if s.isEmpty():
                    return False
                else:
                    top_s = s.pop()
                    if (top_s == '(' and token != ')') or (top_s == '{' and token != '}') or (
                            top_s == '[' and token != ']'):
                        return False
    return s.isEmpty()


file = open("c++_code.txt", 'r')
str = file.read()
file.close()
print(IsValidSource(str))
