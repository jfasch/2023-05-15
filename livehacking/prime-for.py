import sys


number = int(sys.argv[1])
if number < 1:
    print('geh weg!')
    sys.exit(1)

if number == 1:
    print('not prime')
    sys.exit(0)

for divisor_candidate in range(2, number):
    if number % divisor_candidate == 0:
        print('not prime')
        break
else:
    print('prime')
