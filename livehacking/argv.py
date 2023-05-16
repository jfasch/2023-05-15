import sys

if len(sys.argv) != 2:
    print('geh weg!')
    sys.exit(1)

#print(sys.argv)
print(sys.argv[1], type(sys.argv[1]))
