import argparse
import os
import shutil
import tarfile

parser = argparse.ArgumentParser(description='将指定目录下的所有文件分别打成tar包')
parser.add_argument('-s', required=True, help='要压缩的目录')
parser.add_argument('-d', required=True, help='目标目录')

namespace = parser.parse_args()


srcdir = namespace.s
print(srcdir)
path = os.listdir(srcdir)
os.chdir(srcdir)

for file in path:
    #os.chdir(namespace.d)
    print(file,'start')
    tar = tarfile.open(namespace.d + file + '.tar',"w")
    tar.add(namespace.s + file, recursive=False, arcname=file)
    tar.close()
    print(file,'done')
