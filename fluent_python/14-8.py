'''
列表推导式和生成器表达式
演示了生成器的惰性求值能力
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
