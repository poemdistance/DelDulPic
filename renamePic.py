import os
import stat
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

        dot = ''
        name = sys.argv[len(sys.argv)-1].split('.')
        for s in name:
            if s == '':
                dot += '.'

    for n in range(1, length):
        files = os.listdir(sys.argv[n])
        for f in files:
            f = os.path.join(sys.argv[n], f)
            name = f.split('.')
            if name[len(name)-1] == 'mp4' \
                    or name[len(name)-1] == 'jpg' \
                    or name[len(name)-1] == 'jpeg' \
                    or name[len(name)-1] == 'png' \
            :
                dst = name[len(name)-2]+'tmp'+'.'+name[len(name)-1]

                dst = dot + dst

                #先文件名后面添加tmp生成临时文件名
                #防止可能会覆盖掉相同的文件名
                os.rename(f, dst)

        files = os.listdir(sys.argv[n])
        for f in files:
            f = os.path.join(sys.argv[n], f)
            name = f.split('.')
            if name[len(name)-1] == 'mp4' \
                    or name[len(name)-1] == 'jpg' \
                    or name[len(name)-1] == 'jpeg' \
                    or name[len(name)-1] == 'png' \
            :
                dst = str(i) + '.' + name[len(name)-1]
                dst = os.path.join( sys.argv[n], dst )

                #以序号重命名文件
                os.rename(f,dst)
                i += 1

    with open('endNum', 'w') as f:
        f.write(str(i))
