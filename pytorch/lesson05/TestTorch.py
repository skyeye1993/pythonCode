# coding: utf-8 
import torch

a = torch.rand(4, 3, 32, 32)
b = torch.rand(5, 3, 32, 32)
print(torch.cat([a, b], dim=0).shape)  # 在第0个维度上进行拼接

c = torch.rand(4, 4, 32, 32)
print(torch.cat([a, c], dim=1).shape)  # 在第1个维度上进行拼接

a1 = torch.rand(4, 3, 16, 32)
a2 = torch.rand(4, 3, 16, 32)
c = torch.stack([a1, a2], dim=2)
print(c.shape)  # 会创建一个新的维度
aa, bb = c.split([2, 1], dim=1)  # 将3拆成2和1
print(aa.shape, bb.shape)
aa, bb = c.chunk(2, dim=0)  # 将0维度的数据平均拆成两份
print(aa.shape, bb.shape)

# 运算符
a = torch.rand(3, 4)
b = torch.rand(4)
print(torch.equal(a - b, torch.sub(a, b)))
print(torch.equal(a + b, torch.add(a, b)))
print(torch.equal(a * b, torch.mul(a, b)))

# matmul  (a,b)*(c,d) = (ac,bd)  仅限于2d数据
a = torch.tensor([[2., 2.], [2., 2.]])
b = torch.ones(2, 2)
print(torch.matmul(a, b))
print(torch.mm(a, b))
print(a @ b)

a = torch.rand(4, 3, 28, 64)
b = torch.rand(4, 3, 64, 32)
print(torch.matmul(a, b).shape)  # 只对最后两个维度进行扩展
b = torch.rand(4, 1, 64, 32)
print(torch.matmul(a, b).shape)  # 会先对第1个维度进行broadcast，将1扩展为3

a = torch.full([2, 2], 3)
print(a.pow(2))
print(a ** 2)

a = torch.exp(torch.ones([3, 3]))
print(a)

# 范数
a = torch.full([8], 1)
b = a.view(2, 4)
c = a.view(2, 2, 2)
print(a.norm(1), b.norm(1), c.norm(1))  # 第一范数
print(a.norm(2), b.norm(2), c.norm(2))  # 第二范数
print(b.norm(1, dim=1), b.norm(2, dim=1))

a = torch.arange(8).view(2, 4).float()
print(a)
print(a.min(), a.max(), a.mean(), a.prod(), a.sum())  # prod表示累乘
print(a.argmax(), a.argmin())

a = torch.randn(4, 10)
print(a[0])
print(a.argmax())
print(a.argmax(dim=1))
print(a.max(dim=1))
print(a.max(dim=1, keepdim=True))  # keepdim 保持和a的维度相同

print(a.topk(3, dim=1))  # 第一个维度上取前三个最大值
print(a.topk(3, dim=1, largest=False))  # 第一个维度上去前三个最大值

print(a > 0)  # 依次比较每个数是否大于0
print(torch.gt(a, 0))

cond = torch.rand(2, 2)
a = torch.zeros(2, 2)
b = torch.ones(2, 2)
print(cond)
print(a)
print(b)
print(torch.where(cond > 0.5, a, b))  # 依次比较cond中的每一个值，如果大于0.5，选择对应a中的值，否则选b中的值

prob = torch.randn(4, 10)
idx = prob.topk(dim=1, k=3)
print(idx[1])
label = torch.arange(10) + 100
print(label)
torch.gather(label.expand(4, 10), dim=1, index=idx.long())
