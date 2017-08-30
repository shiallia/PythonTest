import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import math
import time

plt.close()  # clf() # 清图  cla() # 清坐标轴 close() # 关窗口
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.axis("equal")  # 设置图像显示的时候XY轴比例
plt.grid(True)  # 添加网格

x = range(10000)
y = range(10000)

ax.scatter(x, y, c='b', marker='.')
plt.show()
time.sleep(2)

x = range(20000)
y = range(20000)

ax.scatter(x, y, c='b', marker='.')
plt.show()
