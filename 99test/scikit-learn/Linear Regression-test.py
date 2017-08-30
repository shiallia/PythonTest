#An illustration of the isotonic regression on generated data.
#The isotonic regression finds a non-decreasing approximation of a function while minimizing the mean squared error on the training data.
#The benefit of such a model is that it does not assume any form for the target function such as linearity
#For comparison a linear regression is also presented.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state
from sklearn import datasets

x = datasets.load_boston().data
y = datasets.load_boston().target
print(type(x))
print(x.shape)
print(type(y))
print(y.shape)

lr = LinearRegression()
lr.fit(x, y)  # x needs to be 2d for LinearRegression

print(lr.coef_)           #打印出计算出来的系数
print(lr.intercept_)      #打印机算出来的截距

k = lr.predict([[0.00632,18,2.31,0,0.538,6.575,65.2,4.09,1,296,15.3,396.9,4.98],
               [0.08829,12.5,7.87,0,0.524,6.012,66.6,5.5605,5,311,15.2,395.6,12.43]])

print(k)
