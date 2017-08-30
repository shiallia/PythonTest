import time
from concurrent.futures import ProcessPoolExecutor, as_completed,ThreadPoolExecutor

NUMBERS = [35, 35, 35, 35, 35, 35, 35, 35]
def fib(n):
   if n<= 2:
       return 1
   return fib(n-1) + fib(n-2)
start = time.time()

def main():
    with ThreadPoolExecutor(max_workers=4) as executor:
        fulture_list = []
        for num in NUMBERS:
            fulture_list.append(executor.submit(fib,num))
        for fulture in as_completed(fulture_list):
            print(fulture.result())
    print('COST: {}'.format(time.time() - start))


if __name__ == '__main__':
    main()
