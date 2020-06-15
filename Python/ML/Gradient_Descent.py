import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
# 创建数据
N = 2000
points = Variable(torch.rand(N,2))
mean_value = torch.mean(points, dim=0)

# 梯度下降
EPOCHS = 1000  # 迭代总次数
LOSS_MIN = 0.0001  # loss的目标最小值，当loss小于此值时停止迭代
lr = 0.01
x = Variable(torch.FloatTensor([0., 0.]), requires_grad=True)

cost = []  # 梯度下降(GD)过程中存储loss的值
x_all = []
for i in range(EPOCHS):

    loss = 0
    for i in range(N):
        loss = loss + torch.pow((points[i] - x), 2)
    loss = loss / N
    loss = loss.mean()
    if loss < LOSS_MIN:
        break
    cost.append(loss)
    loss.backward()  #反向传播求梯度
    x.data -= lr * x.grad.data   #梯度下降
    x.grad.data.zero_()
    print('%f %f %f'%(x.data[0], x.data[1], loss.data))


#画出梯度下降曲线
# print(x_all[0])
# w_all = torch.cat(x_all, dim=0).detach().numpy()#np.array(x_all)
# w_all = np.zeros((EPOCHS,2))
# for i in range(EPOCHS):
#     w_all[i][0] = x_all[i].data[0]
#     w_all[i][1] = x_all[i].data[1]
# print(w_all.shape)
# fig = plt.figure()
# ax2 = fig.add_subplot(111, projection='3d')
# ax2.plot_wireframe(np.array([w_all[:,0]]),np.array([w_all[:,1]]),np.array([cost]))
# ax2.set_xlabel("w1")
# ax2.set_ylabel("w2")
# ax2.set_zlabel("loss")
# fig = plt.figure()


# 画出loss-iteration曲线
plt.plot(range(len(cost)), cost)
plt.title('loss')
plt.xlabel('iteration')
plt.ylabel('loss')
plt.show()

print('the true value is [%f, %f]' % (mean_value.data[0], mean_value.data[1]))
print('the estimated value is [%f, %f]' % (x.data[0], x.data[1]))
