import numpy as np

x = np.arange(10)
print(x)
a = x[1:5]
print(a)
y = x[:, np.newaxis]
print(y.shape)
print(y)

#print(x[:, np.newaxis]) #给数组增加维度

print("下面是另外一个例子")
qq = np.array([[1,2],
              [3,4],
              [5,6]
])
print(qq.shape)
print(qq)

ww = q
q[:, np.newaxis, 0]
print(ww.shape)
print(ww)


