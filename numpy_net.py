#使用numpy实现正向传播和反向传播
import numpy as np
import matplotlib.pyplot as plt

#N为数据批量大小，D_in为输入的维度，D_out为输出维度,H为中间层输出个数
N,D_in,H,D_out=64,1000,100,10

x=np.random.randn(N,D_in)
y=np.random.randn(N,D_out)

w1=np.random.randn(D_in,H)
w2=np.random.randn(H,D_out)

learning_rate=1e-6

loss_p=list()

for t in range(500):
    h=x.dot(w1)
    h_relu=np.maximum(h,0)
    y_pred=h_relu.dot(w2)

    loss=np.square(y_pred-y).sum()
    loss_p.append(loss)
    print("epoches:",t+1,",   loss:",loss)

    grad_y_pred=2.0*(y_pred-y)
    grad_w2=h_relu.T.dot(grad_y_pred)
    grad_h_relu=grad_y_pred.dot(w2.T)
    grad_h=grad_h_relu.copy()
    grad_h[h<0]=0
    grad_w1=x.T.dot(grad_h)

    w1-=learning_rate*grad_w1
    w2-=learning_rate*grad_w2

x=np.arange(500)
y=loss_p

plt.plot(x,y,)
plt.show()
