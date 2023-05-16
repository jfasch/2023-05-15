import sys

def is_prime(n):
    if n < 1:
        raise ValueError(f'{n} is not ...')

    if n == 1:
        return False

    for divisor_candidate in range(2, n):
        if n % divisor_candidate == 0:
            return False
    else:
        return True


number = int(sys.argv[1])

try:
    if is_prime(number):
        print('prime')
    else:
        print('not prime')
except ValueError:
    print('geh weg!')
    sys.exit(1)

