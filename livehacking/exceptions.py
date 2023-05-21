try:
    f = open('/etc/passwd')
except OSError as e:
    print(e)
else:
    print('passt eh')
finally:
    print('fertig, wurscht wie')
