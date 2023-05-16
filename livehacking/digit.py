import sys

translation_table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    }

try:
    digit = sys.argv[1]
except IndexError as e:
    print(f'Dummbatz: gib eine Zahl als einziges Argument')
    sys.exit(1)

try:
    digit = int(digit)
except ValueError as e:
    print(f'Dummbatz: {sys.argv[1]} ist keine Zahl')
    sys.exit(1)

try:
    print(translation_table[digit])
except KeyError as e:
    print(f'Dummbatz: {sys.argv[1]} ist keine Ziffer')
    sys.exit(1)
