import time
from concurrent.futures import ProcessPoolExecutor, as_completed

NUMBERS = [35, 35, 35, 35, 35, 35, 35, 35]
def fib(n):
   if n<= 2:
       return 1
   return fib(n-1) + fib(n-2)
start = time.time()

def main():
    with ProcessPoolExecutor(max_workers=4) as executor:
       for num, result in zip(NUMBERS, executor.map(fib, NUMBERS)):
           print('fib({}) = {}'.format(num, result))
    print('COST: {}'.format(time.time() - start))


if __name__ == '__main__':
    main()
