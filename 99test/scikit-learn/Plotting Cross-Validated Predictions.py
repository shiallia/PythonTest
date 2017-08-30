#This example shows how to use cross_val_predict to visualize prediction errors
from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt


lr = linear_model.LinearRegression()  #线性回归,LinearRegression()是类的构造函数，lr是类的一个实例
print(type(lr))                       #lr的数据类型是class
boston = datasets.load_boston()       #读取初始数据,bosten.data是原始数据，bosten.target是值
y = boston.target
print(type(boston))                   #boston是一个类
print(type(boston.data))              #boston.data是一个numpy数组
print(type(boston.target))


# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validation:
predicted = cross_val_predict(lr, boston.data, y, cv=5)


fig, ax = plt.subplots()
ax.scatter(y, predicted)                                        #画出散点图
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)    #这是一条y=x的直线，越接近这条直线，表示预测的越准确
ax.set_xlabel('Measured')             #测量值
ax.set_ylabel('Predicted')            #预测值
plt.show()