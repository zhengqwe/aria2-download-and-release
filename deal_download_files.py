import os
from os import path

os.system('rm -rf result')
os.mkdir('result')

for dirpath, dirnames, filenames in os.walk("downloads"):
    for filename in filenames:
        # 压缩文件
        fsize=path.getsize(filename)
        if fsize>1024*1024*1536:
            cmd = '7z a -t7z -m0=Copy -sccUTF-8 -v1536m -sdel "{afile}" "{sourcefile}"'.format(
                afile=path.join('./result', filename + '.7z'),
                sourcefile=path.join(dirpath, filename)
            )
        else:
            cmd = '7z a -t7z -m0=Copy -sccUTF-8 -sdel "{afile}" "{sourcefile}"'.format(
                afile=path.join('./result', filename + '.7z'),
                sourcefile=path.join(dirpath, filename)
            )
        print("[deal] %s with %s" % (path.join(dirpath, filename), cmd))
        os.system(cmd)
