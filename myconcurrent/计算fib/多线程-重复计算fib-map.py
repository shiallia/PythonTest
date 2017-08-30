import time
from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor

NUMBERS = [34, 33, 34, 33, 34, 33, 34, 33]


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        # 这里executor.map()是一个迭代器，哪个线程先结束，就yield那个future的result
        for num, result in zip(NUMBERS, executor.map(fib, NUMBERS)):
            print('fib({}) = {}'.format(num, result))
    print(f'COST: {format(time.time() - start)}')


if __name__ == '__main__':
    main()
