

lista = [1, 2, 3]


def changelist1(l):
    '''
    这个是赋值操作，函数内部的l跟外部的l指向了不同的列表
    '''
    l = ['a', 'b', 'c']
    print(l)


def changelist2(l):
    '''
    这个是赋值操作，函数内部的l跟外部的l指向了不同的列表
    '''
    l = l + ['a']
    print(l)


def changelist3(l):
    '''
    这个是修改操作，函数内部的l跟外部的l，还是指向同一个列表
    '''
    l += ['b']
    print(l)


def changelist4():
    '''
    这是个赋值操作，函数内部的lista跟函数外部的lista，指向了不同的列表
    '''
    lista = ['a', 'b', 'c']
    print(lista)

def changelist5():
    '''
    这是个赋值操作，因为使用了global，函数内部和外部使用的是同一个列表
    '''
    global lista
    lista = ['哈','哈']
    print(lista)


changelist1(lista)
print(lista)

changelist2(lista)
print(lista)

changelist3(lista)
print(lista)

changelist4()
print(lista)

changelist5()
print(lista)



