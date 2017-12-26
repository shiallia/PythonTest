'''
*运算符可以把可迭代对象拆开作为函数的参数
函数返回的多个对象会作为一个元组，可以赋值给多个对象
在处理函数的返回值的之后，_可以作为占位符，*可以处理剩下的元素
'''
print(divmod(20, 8))

t = (20, 8)
print(divmod(*t))

a, b = divmod(*t)
print(a)
print(b)


a, *body, c, d = range(5)
print(a)
print(body)
print(c)
print(d)

