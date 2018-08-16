'''
全局变量的另一种用法，globles()会返回一个字典，里面有所有的全局变量
'''


a = 3
b = 4

def testFunc():
    globals()['a'] = 20


testFunc()

print(a)