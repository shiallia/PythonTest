import tarfile
import os
 
#创建压缩包名
tar = tarfile.open("/tmp/tartest.tar.gz","w")
#创建压缩包
for root,dir,files in os.walk("/tmp/tartest"):
    for file in files:
        fullpath = os.path.join(root,file)
        tar.add(fullpath)
tar.close()

rootdir = ""
