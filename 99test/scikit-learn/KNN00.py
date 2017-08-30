from sklearn.neighbors import NearestNeighbors
import numpy as np

#定义一个数组
X = np.array([[-1,-1],
              [-2,-1],
              [-3,-2],
              [1,1],
              [2,1],
              [3,2]
              ])
"""
NearestNeighbors用到的参数解释
n_neighbors=5,默认值为5，表示查询k个最近邻的数目
algorithm='auto',指定用于计算最近邻的算法，auto表示试图采用最适合的算法计算最近邻
fit(X)表示用X来训练算法
"""
nbrs = NearestNeighbors(n_neighbors=3, algorithm="ball_tree").fit(X)
# 返回距离每个点k个最近的点和距离指数，indices可以理解为表示点的下标，distances为距离
distances, indices = nbrs.kneighbors(np.array([1, 0.5]))
print(indices)
print(distances)

print(nbrs.kneighbors_graph(np.array([[1, 0.5],[3,2]])).toarray())
