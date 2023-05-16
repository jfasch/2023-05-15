import math

def sine(nparts):
    step = 2*math.pi / nparts
    x = 0
    while True:
        yield x, int(math.sin(x) * 20) + 20
        x += step

for x, y in sine(10):
    if y <= 20:
        numstars = 20 - y
        print(('*'*numstars).rjust(20))
    else:
        numstars = y - 20
        print(' '*20 + '*'*numstars)
