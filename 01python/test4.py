#关键字参数
#关键字参数可以使参数的顺序变得不重要
def printinfo( name, age ):
   "打印任何传入的字符串"
   print("Name: ", name)
   print("Age ", age)
   return

#调用printinfo函数
print("演示关键字参数")
printinfo( age=50, name="miki" )
print("\n\n")


# 缺省参数
# 调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：

def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print("Name: ", name)
   print("Age ", age)
   return

#调用printinfo函数
print("演示缺省参数")
printinfo( age=50, name="miki" )
printinfo( name="miki" )
print("\n\n")


#不定长参数
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print("输出: ")
   print(arg1)
   print(type(vartuple))
   for var in vartuple:
      print(var)
   return

# 调用printinfo 函数
print("演示不定长参数：")
printinfo( 10 )
printinfo( 70, 60, 50 )
print("\n\n")


#lambda函数
# 可写函数说明
sum = lambda x, y: x + y;

# 调用sum函数
print("演示lambda函数：")
print("相加后的值为 : ", sum( 10, 20 ))
print("相加后的值为 : ", sum( 20, 20 ))
print("\n\n")


#局部变量和全局变量

total = 0 # 这是一个全局变量
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2 # total在这里是局部变量.
   print("函数内是局部变量 : ", total)
   return total

#调用sum函数
print("演示局部变量和全局变量")
sum( 10, 20 )
print("函数外是全局变量 : ", total)
print("\n\n")



#函数内部使用全局变量，global关键字：
Money = 2000
def AddMoney():
   global Money
   Money = Money + 1

print("演示global关键字")
print(Money)
AddMoney()
print(Money)
print("\n\n")



