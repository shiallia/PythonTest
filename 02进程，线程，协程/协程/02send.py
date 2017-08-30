"""
其中next(sfib)相当于sfib.send(None)，可以使得sfib运行至第一个yield处返回。
后续的sfib.send(random.uniform(0, 0.5))则将一个随机的秒数发送给sfib，作为当前中断的yield表达式的返回值。
这样，我们可以从“主”程序中控制协程计算斐波那契数列时的思考时间，协程可以返回给“主”程序计算结果，Perfect！
"""

import time
import random


def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        print(f"第{index}次运行循环")
        sleep_cnt = yield b
        print(f"第{index}次运行循环完毕")
        print('let me think {0} secs'.format(sleep_cnt))
        time.sleep(sleep_cnt)
        a, b = b, a + b
        index += 1

def method1():
    print('-'*10 + 'test yield send' + '-'*10)
    sfib = stupid_fib(10)
    print(next(sfib))
    print(sfib.send(3))
    print(sfib.send(3))

def method2():
    sfib = stupid_fib(10)
    print(next(sfib))
    while True:
        print(fib_res)
        try:
            fib_res = sfib.send(random.uniform(0, 3))
        except StopIteration:
            break

if __name__ == '__main__':
    method1()
