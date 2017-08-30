import time
from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor

NUMBERS = [34, 33, 34, 33, 34, 33, 34, 33]


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    with ThreadPoolExecutor(max_workers=4) as executor:
        start = time.time()
        fulture_list = []
        for num in NUMBERS:
            fulture_list.append(executor.submit(fib, num))
        # as_completed()函数是一个生成器，接受一个future列表作为参数。这样，谁先返回就先迭代谁
        for future in as_completed(fulture_list):
            print(future.result())
    print('COST: {}'.format(time.time() - start))


if __name__ == '__main__':
    main()
