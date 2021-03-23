
'''
@File    :   helloworld.py
@Time    :   2021/03/23 19:32:15
@Author  :   mike.wu 
@Contact :   xcwu@whu.edu.cn
@github:    https://github.com/wxcon
'''

from sklearn.neighbors import NearestNeighbors 
import numpy as np 
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
nbrs = NearestNeighbors(n_neighbors = 2, algorithm='ball_tree').fit(X)

distances, indices = nbrs.kneighbors(X)
print(distances) 
print(indices) 

print(nbrs.kneighbors_graph(X).toarray())
