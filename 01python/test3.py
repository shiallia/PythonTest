# while,break,continue和其他语言没有区别
print("while的循环")
i = 1
while i < 10:
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print(i)         # 输出双数2、4、6、8、10

i = 1
while 1:            # 循环条件为1必定成立
    print(i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

print("\n\n")


# while使用else语句
print("while使用else语句")
count = 0
while(count < 5):
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")

print("\n\n")


#for循环
print("for循环")
for letter in 'Python':     # 第一个实例
   print('当前字母 :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print('当前 :', fruit)

print("\n\n")

#通过序列索引迭代
print("序列索引迭代")
fruits = ['banana', 'apple',  'mango']
print(len(fruits))
print(range(len(fruits)))
for index in range(len(fruits)):
   print('当前水果 :', fruits[index])

print("\n\n")

#求出10--20之间的质数
print("求出10--20之间的质数")
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print(num, '是一个质数')
print("\n\n")

