

try:
    a = int("zhangfan")
    b = 2
except Exception as e:
    print(e)
    #print(b)    #这个b是打印不了的，因为在上一个代码块
else:
    print('这里是没有发生异常的时候，才会执行的代码')
finally:
    print('这里是无论如何偶会执行的代码')






