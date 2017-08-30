# 1.python的算数运算符

a = 21
b = 10
c = 0

print("python的算数运算符")

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b                     #得到的是浮点数
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b                      #a的b次幂
print("6 - c 的值为：", c)

a = 10
b = 5
c = a//b                      #得到的是整形
print("7 - c 的值为：", c)
print("\n\n")

# 2.python的逻辑运算符
a = 0
b = 10
print("逻辑运算符")
if ( a and b ):
   print("1 - 变量 a 和 b 都为 true")
else:
   print("1 - 变量 a 和 b 有一个不为 true")

if ( a or b ):
   print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print("2 - 变量 a 和 b 都不为 true")

if not( a and b ):
   print("3 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
   print("3 - 变量 a 和 b 都为 true")

print("\n\n")


# 3.python成员运算符

a = 2
b = 20
list = [1, 2, 3, 4, 5 ];

print("成员运算符")
if ( a in list ):
   print("1 - 变量 a 在给定的列表中 list 中")
else:
   print("1 - 变量 a 不在给定的列表中 list 中")

if ( b not in list ):
   print("2 - 变量 b 不在给定的列表中 list 中")
else:
   print("2 - 变量 b 在给定的列表中 list 中")
print("\n\n")


# 4.Python身份运算符
# 身份运算符用于比较两个对象的存储单元

a = 20
b = 20

print("python的身份标识符")
if ( a is b ):
   print("1 - a 和 b 有相同的标识")
else:
   print("1 - a 和 b 没有相同的标识")

if ( id(a) == id(b) ):
   print("2 - a 和 b 有相同的标识")
else:
   print("2 - a 和 b 没有相同的标识")







