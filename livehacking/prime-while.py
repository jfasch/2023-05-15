import sys


number = int(sys.argv[1])
if number < 1:
    print('geh weg!')
    sys.exit(1)

if number == 1:
    print('not prime')
    sys.exit(0)

divisor_candidate = 2
while divisor_candidate < number:
    if number % divisor_candidate == 0:
        print('not prime')
        break
    divisor_candidate += 1
else:
    print('prime')
