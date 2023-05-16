def fibonacci():
    first, second = 1, 1

    print('first')
    yield first
    print('second')
    yield second

    while True:
        third = first + second
        print('third')
        yield third
        first, second = second, third

if __name__ == '__main__':
    for n in fibonacci():
        print(n)
