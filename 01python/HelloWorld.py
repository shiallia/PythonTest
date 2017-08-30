# -*- coding: utf-8 -*-

' a test module '

__author__ = '张帆'

import sys
from PIL import Image


#class
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

stu = Student('zhangfan',100)
print(stu.name,stu.score)
print(stu.get_grade())




#python的序列化和反序列化
import pickle

d = {'name': 'Bob', 'age': 20, 'score': 88}
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)


#序列化或者反序列化为json
import json
json_Str=json.dumps(d)
print(json_Str)
d=json.loads(json_Str)
print(d)

#新进程
# from multiprocessing import Process
# import  os
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')





def test():
    im = Image.open("1.jpg")
    print(im.format, im.size, im.mode)
    im.thumbnail((200, 100))
    im.save('thumb.jpg', 'PNG')

if __name__=='__main__':
    test()
