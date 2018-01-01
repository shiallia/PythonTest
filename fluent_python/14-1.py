'''
解释器需要迭代对象x是的时候，会自动调用iter(x)
内置的iter函数有如下作用：
1检查对象是否实现了__iter__方法，如果实现了就调用他，获取一个迭代器
2如果没有实现，但是实现了__getitem__方法，解释器会创建一个迭代器，尝试按顺序(从索引0开始)获取元素
3如果尝试失败，会抛出异常
本例对应情况2
'''
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)



s = Sentence('hello world everyone')
print(s)

for word in s:
    print(word)

print(list(s))


print(type(iter(s)))

