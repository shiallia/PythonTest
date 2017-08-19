
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time


def return_future(msg):
    time.sleep(3)
    return msg


# 创建一个线程池
pool = ThreadPoolExecutor(max_workers=2)
pool = ProcessPoolExecutor

# 往线程池加入2个task
f1 = pool.submit(return_future, 'hello')
f2 = pool.submit(return_future, 'world')

# print(f1.done())
# print(f2.done())
# time.sleep(3)
# print(f1.done())
# print(f2.done())

print(f1.result())
print(f2.result())
