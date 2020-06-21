# coding: utf-8 
import torch
import time

print(torch.__version__)
print(torch.cuda.is_available())

a = torch.randn(10000, 1000)  # 矩阵维度10000*1000
b = torch.randn(1000, 2000)

t0 = time.time()
c = torch.matmul(a, b)  # 矩阵a * b
t1 = time.time()
print(a.device, t1 - t0, c.norm(2))

device = torch.device('cuda')
a = a.to(device)
b = b.to(device)

t0 = time.time()
c = torch.matmul(a, b)
t2 = time.time()
print(a.device, t2 - t0, c.norm(2))  #第一次调用GPU加速时会初始化各类参数，所以速度会慢

t0 = time.time()
c = torch.matmul(a, b)
t2 = time.time()
print(a.device, t2 - t0, c.norm(2))
