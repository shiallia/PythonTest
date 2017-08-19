from sklearn.preprocessing import  PolynomialFeatures
import numpy as np

x = np.arange(6).reshape(3,2)
print(x)

poly = PolynomialFeatures(degree=2)
test = poly.fit_transform(x)
print(poly)
print(test)