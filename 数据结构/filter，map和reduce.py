from functools import reduce

#map,并行遍历
a = [1, 3, 5]
b = [2, 4, 6]
list_a = list(map(lambda x, y: x*y, a, b))
print(list_a)

#filter过滤列表，符合条件的，返回新列表
list_b = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(list_b)


#reduce归并,这个函数现在在functools里面
list_c = reduce(lambda x, y: x+y, range(100))
print(list_c)
