'''
生成器函数__iter__
调用这个函数会返回一个生成器对象
next(生成器对象)可以产出值
'''
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        for word in self.words:
            yield word

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

