import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))
sc = plt.scatter(1,2,3,4,5,6,7,8)
pl = plt.plot([3,4,5],[2,3,4])

print(type(sc))
print(type(pl))
print(pl)
plt.show()
