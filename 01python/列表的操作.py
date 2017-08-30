#第一种生成列表的方式
#这里面有个副作用，创建完列表后，i仍然存在
list_a = []
for i in range(5):
    list_a.append(i*i)
print(i)
print(list_a)

#第二种生成列表的方式
#lambda x: x**2表示一个函数，返回参数的平方
#函数接受一个函数类型参数、一个或者多个可迭代对象参数，返回一个可迭代器，此迭代器中每个元素，均是函数参数实例调用可迭代对象后的结果。
#list构造函数根据可迭代对象生成列表
list_b = list(map(lambda x: x**2, range(6)))
temp = map(lambda x: x**2, range(6))
print(type(temp))
print(list_b)

#第三种生成列表的方式,这种方式最简介
#这种方法叫列表生成器
list_c = [x**2 for x in range(10)]
print(list_c)

#同时需要下标和值的迭代
# enumerate()是python的内置函数
# enumerate在字典上是枚举、列举的意思
# 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
a = enumerate(x*x for x in range(5))
for index, item in a:
    print(index, item)
print(type(a))


#多列表并行迭代
for x, y in zip([1, 2, 3], [10, 20, 30]):
    print(x, y)


# 凡是可以for循环的，都是Iterable
# 凡是可以next()的，都是Iterator
# 集合数据类型如list，truple，dict，str，都是Itrable不是Iterator，但可以通过iter()函数获得一个Iterator对象


