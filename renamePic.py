import os
import sys

length = len(sys.argv)
if length < 2:
    print('Please input scan dir param')
    os._exit
else:
    i = 1
    if os.path.exists('endNum'):
        f = open('endNum')
        i = int(f.read())
        f.close()

    for n in range(1, length):
        files = os.listdir(sys.argv[n])
        for f in files:
            f = os.path.join(sys.argv[n], f)
            name = f.split('.')
            if name[1] != 'py':
                os.rename(f, name[0]+'tmp'+'.'+name[1])

        files = os.listdir(sys.argv[n])
        for f in files:
            f = os.path.join(sys.argv[n], f)
            name = f.split('.')
            if name[1] != 'py':
                os.rename(f, os.path.join(sys.argv[n], str(i)+'.'+name[1]))
                i += 1

    with open('endNum', 'w') as f:
        f.write(str(i))
