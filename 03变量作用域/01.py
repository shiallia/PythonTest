"""
这个例子说明:
1.python顺序执行模块里面的语句，if __name__ == '__main__':只在程序作为主模块的时候运行，所以可以调用main函数，或者初始化部分全局变量
2.if __name__ == '__main__':一般放在文件最后面，免得找不到main函数
3.在这种结构下main()函数使用的函数和全局变量定义的位置无所谓
"""



<<<<<<< HEAD
def test(a, b):
=======
def test(a,b):
>>>>>>> origin/master
    pass


def main():
    global a
    a = a + 1
    print(a)
<<<<<<< HEAD
    test(1, 2)
    test2(1, 2)
=======
    test(1,2)
    test2(1,2)
>>>>>>> origin/master

def test2():
    pass

if __name__ == '__main__':
<<<<<<< HEAD
    a = 3
=======
    a=3
>>>>>>> origin/master
    main()





