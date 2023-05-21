import contextlib

@contextlib.contextmanager
def PrefixPrint(prefix):
    def my_print(*args, **kwargs):
        my_args = (prefix,) + args
        orig_print(*my_args, **kwargs)

    global print
    orig_print = print
    print = my_print

    yield

    print = orig_print

print('good old print')
with PrefixPrint('MEGA: '):
    print('hey super!')
print('boring old print')
