import random

ntries = 0
while ntries < 8:
    eyes = random.randrange(1,7)
    ntries += 1
    if eyes == 6:
        print('hooray')
        break
else:
    print('loose')

