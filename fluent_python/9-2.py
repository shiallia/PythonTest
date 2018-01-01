'''
obj.__dict__     查看实例属性
'''
from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)

    @classmethod
    def frombytes(cls, octets):
        typcode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typcode)
        return cls(*memv)
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    
    def __iter__(self):
        return (i for i in (self._x, self._y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self._x, self._y)

    def __bool__(self):
        return bool(abs(self))



test  = Vector2d(3, 5)
print(test)
print(bool(test))
print(abs(test))

for i in test:
    print(i)


hehe = bytes(test)
haha = Vector2d.frombytes(hehe)
print(haha)

print(test.__dict__)

print(dir())
print(__file__)
print(globals())


