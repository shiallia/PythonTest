

# 解释器调用可迭代对象'abc'的生成器函数__iter__，获得了一个生成器对象，这个生成器对象，依次产出了a b c
for i in 'abc':
    print(i)

# iter('abc')是一个生成器对象，解释器调用这个对象的__iter__方法，返回了这个对象自身
for i in iter('abc'):
    print(i)

# enumerate()的参数是任意可迭代对象，产出两个元素组成的元组，结构是(index，item)
for i,j in enumerate('abc'):
    print(i,j)

