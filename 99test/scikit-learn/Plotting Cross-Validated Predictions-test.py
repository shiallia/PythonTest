#An illustration of the isotonic regression on generated data.
#The isotonic regression finds a non-decreasing approximation of a function while minimizing the mean squared error on the training data.
#The benefit of such a model is that it does not assume any form for the target function such as linearity
#For comparison a linear regression is also presented.
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.utils import check_random_state

n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50. * np.log(1 + np.arange(n))


lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)  # x needs to be 2d for LinearRegression




fig = plt.figure()
plt.plot(x, y, 'r.', markersize=12)               #画第一条线
plt.plot(x, y_, 'g.-', markersize=12)             #画第二条线
plt.plot(x, lr.predict(x[:, np.newaxis]), 'b-')   #画第三条线
plt.gca().add_collection(lc)
plt.legend(('Data', 'Isotonic Fit', 'Linear Fit'), loc='lower right')
plt.title('Isotonic regression')
plt.show()
