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
a = enumerate(x*x for x in range(5))
for i,x in a:
    print(i, x)
print(type(a))


#多列表并行迭代
for x,y in zip([1,2,3],[10,20,30]):
    print(x, y)



