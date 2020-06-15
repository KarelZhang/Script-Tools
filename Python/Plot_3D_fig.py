import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
import os
x_1 = np.zeros(1000)
x_2 = np.zeros(1000)
loss = np.zeros(1000)
file = open('log.txt')
lines = file.readlines()
print(len(lines))
for i in range(len(lines)):
    line = lines[i].replace('\n','')
    items = line.split(' ')
    x_1[i] = float(items[0])
    x_2[i] = float(items[1])
    loss[i] = float(items[2])
    # print(line)
fig = plt.figure()
ax2 = fig.add_subplot(111, projection='3d')
ax2.plot_wireframe(np.array([x_1]),np.array([x_2]),np.array([loss]))
ax2.set_xlabel("w1")
ax2.set_ylabel("w2")
ax2.set_zlabel("loss")

plt.show()
