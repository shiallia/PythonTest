# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#plot是线图

x = np.linspace(0, 10, 10000)
y = np.sin(x)
z = np.cos(x**2)
ss = np.tan(x)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z ,"ro",markersize=1,linewidth=100,label="$cos(x^2)$")                     #b-- = black+虚线
plt.plot(x,ss,label="$tan(x)$",color="green")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,3)
plt.legend()                                                #显示图例
plt.show()
