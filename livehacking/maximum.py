import sys

lhs, rhs = eval(sys.argv[1]), eval(sys.argv[2])
print(rhs if lhs < rhs else lhs)
