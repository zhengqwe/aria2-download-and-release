import os
from os import path

os.system('rm -rf result')
os.mkdir('result')

for dirpath, dirnames, filenames in os.walk("downloads"):
    os.chdir(dirpath)
    for filename in filenames:
        # 压缩文件
        cmd = '7z a -t7z -m0=Copy -sccUTF-8 -v1024m -sdel "{afile}" "{sourcefile}"'.format(
            afile=path.join('../result', filename + '.7z'),
            sourcefile=filename
        )
        print("[deal] %s with %s" % (path.join(dirpath, filename), cmd))
        os.system(cmd)
        # 删除原始文件
    os.chdir('..')
