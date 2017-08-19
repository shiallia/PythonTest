import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np

lena = mpimg.imread('123.png') # 读取和代码处于同一目录下的 lena.png
# # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
# lena.shape #(512, 512, 3)

fig1 = plt.figure('fig1')
plt.imshow(lena) # 显示图片
fig2 = plt.figure('fig2')
plt.imshow(lena)
plt.figure(2)
plt.ylim(0,20)
plt.figure(1)
plt.ylim(0, 40)

#plt.axis('off') # 不显示坐标轴
plt.show()
