from infix_to_postfix import *
from Evaluate import *

str = "120 + 35 * 31 ^ 2 / 13 - 5"
str = infix_to_postfix(str)
str = evaluation(str)
print(str)
