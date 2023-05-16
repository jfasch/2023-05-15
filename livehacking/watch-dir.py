import os, sys, time
import pandas


def watch_dir(dirname):
    seen = set()

    while True:
        fullnames = sorted((os.path.join(dirname, fn) for fn in os.listdir(dirname)))

        for fn in fullnames:
            if fn in seen:
                continue

            seen.add(fn)
            df = pandas.read_csv(fn)
            yield fn, df

        time.sleep(1)

def one_dataset(filename):
    return [
        (filename,
         pandas.DataFrame({
             'ID': ['5', '3', '7'],
             'Firstname': ['Joerg', 'Sepp', 'Elizabeth, II'],
             'Lastname': ['Faschingbauer', 'Huber', 'Queen'],
         })),
    ]


dirname = sys.argv[1]
testing = eval(sys.argv[2])

if not testing:
    data = watch_dir(dirname)
else:
    data = one_dataset('dummy1')

for filename, df in data:
    print('-'*20, filename)
    print(df)

