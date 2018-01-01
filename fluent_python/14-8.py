'''
列表推导式和生成器表达式
演示了生成器的惰性求值能力
只要python函数体中有yield关键字，该函数就是生成器函数
调用生成器函数，会返回一个生成器对象。也就是说，生成器函数是生成器工厂
'''

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')



res1 = [x*3 for x in gen_AB()]

print('-----------------')

for i in res1:
    print(f'-->{i}')

print('++++++++++++++++++')
res2 = (x*3 for x in gen_AB())

print('*********************')

for i in res2:
    print(f'-->{i}')



print(gen_AB)
print(gen_AB())
