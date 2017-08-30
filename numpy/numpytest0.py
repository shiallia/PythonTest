import numpy as np
import matplotlib.pyplot as plt

#1.先创建python列表，再通过函数转换成numpy数组
a = np.array([1, 2, 3, 4])
b = np.array((5, 6, 7, 8))
c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
print(b)
print(c)

print(type(c))

print('现在的数组大小',c.dtype)
print(c.shape)
print('改变数组shape',c.dtype)
c.shape = 4,3
print(c)

#创建一个改变了尺寸的新数组，原数组的shape保持不变
d = a.reshape((2, 2))
print(d)

#2.专门函数创建数组
#arange函数类似于python的range函数，通过指定开始值、终值和步长来创建一维数组，注意数组不包括终值
rangetest = np.arange(0,1,0.1)
print(rangetest)

#linspace函数通过指定开始值、终值和元素个数来创建一维数组，可以通过endpoint关键字指定是否包括终值，缺省设置是包括终值:
linspacetest = np.linspace(0, 1, 12)
print(linspacetest)

#logspace函数和linspace类似，不过它创建等比数列，下面的例子产生1(10^0)到100(10^2)、有20个元素的等比数列:
logspacetest = np.logspace(0, 2, 20)
print(logspacetest)
print(logspacetest.dtype)


d = np.zeros((3,4,5))
print(d)
print(d.itemsize)
