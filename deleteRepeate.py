import hashlib
import shutil
import os

def getHash(filePath):

    md5 = hashlib.md5()
    with open(filePath, 'rb') as f:
        md5.update(f.read())
        val = md5.hexdigest()

    return val

def Traversing(path):
    global num
    x = 0
    dirlist = os.listdir(path)
    for f in dirlist:
        f = path + f;
        Val = getHash(f)
        try:
            if hashTable[Val] == 1:
                print('Found same file %s, deleting it...' % f)

                dst = f
                if os.path.exists(f):
                    dst = f + '_'+str(x)

                shutil.move(f, 
                        os.path.expanduser('~')+'/.local/share/Trash/files/dst')
                x += 1
        except KeyError:
            hashTable[Val] = 1
            num += 1

path1 = './tst/'
path2 = './pic/'

num = 0
hashTable = { }
Traversing(path1)
Traversing(path2)
print(num)
