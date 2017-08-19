import os
#print(os.name)
#print(os.environ)


#r 只读
#w 只写，若文件不存在则创建，如果文件存在，则截断（清空）文件
#a 追加写，如果文件不存在，则创建文件
#r+ 可读可写
#w+ 可读可写,若文件不存在则创建，如果文件存在，则截断（清空）文件
#a+ 追加打开文件，可读可写，如果文件不存在，则创建文件
with open("filetest.txt","r") as fr:
    #print(fr.read())
    print(fr.readline())
    print(fr.readline())
    print(fr.readline())



fw = open("filetest.txt", "w+")
fw.write("hehe\n")
fw.write("hehe")
fw.close()
#
# fr = open("d:/222.txt","r")
# print(fr.read())
# fr.close()

