"""
当一个函数中包含yield语句时，python会自动将其识别为一个生成器
yield在这里可以保留fib函数的计算现场，暂停fib的计算并将b返回
而将fib放入for…in循环中时，每次循环都会调用next(fib())，
唤醒生成器，执行到下一个yield语句处，直到抛出StopIteration异常,
此异常会被for循环捕获，导致跳出循环。
"""

def fib():
    a = 0
    while True:
        if a == 10:
            return
        c = yield 2*a
        print(f"生成器内部收到外面传来的值：{str(c)}")
        a += 1


def method1():
    #使用方法1，先调用一次next，再调用send，send可以向generator里面传值
    fun = fib()
    print(next(fun))
    print(f"生成器返回的值是：{fun.send(10)}")
    print(f"生成器返回的值是：{fun.send(20)}")

def method2():
    #使用方法2，用for循环
    for i in fib():
        print(i)

if __name__ == '__main__':
    method1()
    method2()
