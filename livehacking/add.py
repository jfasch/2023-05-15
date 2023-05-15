import sys

print('argv:', sys.argv)

if len(sys.argv) != 3:
    print('dummbatz!')
    sys.exit(1)

lhs = int(sys.argv[1])
rhs = int(sys.argv[2])

summe = lhs + rhs
print(summe)
