# 激活函数
import torch
from torch.nn import functional as F

a = torch.linspace(-100, 100, 10)
print(a)
print(torch.sigmoid(a))
print(torch.tanh(a))
print(torch.relu(a))

x = torch.ones(1)
w = torch.full([1], 2)
mse = F.mse_loss(torch.ones(1), x * w)  # (1-w*x)的平方
print(mse)

w.requires_grad_()
mse = F.mse_loss(torch.ones(1), x * w)
print(torch.autograd.grad(mse, [w]))  # (1-w*x)的平方 对w求偏导的值

mse = F.mse_loss(torch.ones(1), x * w)
mse.backward()
print(w.grad)

# softmax  梯度
a = torch.rand(3)
a.requires_grad_()

p = F.softmax(a, dim=0)
print(torch.autograd.grad(p[1], [a], retain_graph=True))
print(torch.autograd.grad(p[2], [a]))

# 梯度感知机
x = torch.randn(1, 10)
w = torch.randn(1, 10, requires_grad=True)
o = torch.sigmoid(x @ w.t())
loss = F.mse_loss(torch.ones(1, 1), o)
loss.backward()
print(w.grad)


# 多输出感知机
x = torch.randn(1, 10)
w = torch.randn(2, 10, requires_grad=True)
o = torch.sigmoid(x @ w.t())
loss = F.mse_loss(torch.ones(1, 2), o)
loss.backward()
print(w.grad)
