#这个系列的例子可以看出，cpu密集型计算，必须使用多进程

import time
from concurrent.futures import ProcessPoolExecutor

NUMBERS = [34, 33, 34, 33, 34, 33, 34, 33]


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        for num, result in zip(NUMBERS, executor.map(fib, NUMBERS)):
            print('fib({}) = {}'.format(num, result))
    print('COST: {}'.format(time.time() - start))


if __name__ == '__main__':
    main()
