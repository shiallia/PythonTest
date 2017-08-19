str1 = "hello world"
#c风格的转义字符
str2 = "hello \"world\""
#python风格的处理方式
str3 = 'hello "world"'
#三引号可以支持字符串的换行
str4 = '''hello
    world'''
#忽略转义字符
str5 = r"hello \"world\""

print(str2)
print(str3)
print(str4)
print(str5)

#通过索引访问字符串里面的字符
print(str2[0])

mystr = "my name is zhangan and i am learing python"

print(mystr.find("name"))

