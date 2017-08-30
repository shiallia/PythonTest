#定义一个类
class Employee:
   '所有员工的基类'
   empCount = 0  #类变量，在类的所有实例之间共享
   __privateCount = 0   #类的私有变量，不能在类的外面访问

   def __init__(self, name, salary):      #构造函数
      self.name = name
      self.salary = salary
      self.empCount += 1
      self.__privateCount += 1

   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)

#演示一个基本的类
print("演示一个基本的类：")
zhangfan = Employee("zhangfan",100)
print(Employee.empCount,zhangfan.name,zhangfan.salary)
zhangfan.age = "100岁"                #实例属性
print(zhangfan.age)
del zhangfan.age
print(Employee._Employee__privateCount)  #可以通过这种方式访问类的私有变量
print("\n\n")

#类的内置属性
print("下面这些是类的内置属性")
print("Employee.__doc__:", zhangfan.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
print("\n\n")


#类的运算符重载
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):   #改变了print的行为
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self,other):    #改变了+的行文
      return Vector(self.a + other.a, self.b + other.b)

print("演示运算符重载")
v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2)
print("\n\n")