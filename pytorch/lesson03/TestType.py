# coding: utf-8 
import torch
import numpy as np

a = torch.randn(2, 3)
print(a.type())
print(type(a))
print(isinstance(a, torch.FloatTensor))
data = torch.rand([2, 3], dtype=torch.double)
print(isinstance(data, torch.cuda.DoubleTensor))
data = data.cuda()
print(isinstance(data, torch.cuda.DoubleTensor))
a = np.array([2, 3.3])
print(a)
print(torch.from_numpy(a))
a = np.ones([2, 3])
print(torch.from_numpy(a))
print(torch.tensor([2, 3]))  # 数据是[2,3]
print(torch.tensor([[2, 3], [4.1, 5.2]]))
print(torch.empty(1))
print(torch.Tensor(2, 3))
print(torch.IntTensor(2, 3))
print(torch.FloatTensor(2, 3))  # 维度是2*3
print(torch.tensor([1.2, 3]).type())
torch.set_default_tensor_type(torch.DoubleTensor)  # 将pytorch默认的tensor类型设置为Double
a = torch.randn(3, 3)
print(a)
print(torch.rand_like(a))  # 构造一个和a维度相同的矩阵
print(torch.randint(1, 10, [3, 4]))  # 构造一个3*4的矩阵，每个值大于等予1小于10
print(torch.full([2, 3], 7))  # 维度2*3 每个值为7
print(torch.arange(0, 10))
print(torch.arange(0, 10, 2))

print(torch.linspace(0, 10, steps=4))
print(torch.logspace(0, -1, steps=10))

print(torch.eye(3, 3))  # 生成单位矩阵

print(torch.randperm(10))  # 将0到9随机打断 类似shuffle

# 切片操作
a = torch.randn(4, 3, 28, 28)
print(a[0].shape)
print(a[0, 0].shape)
print(a[0, 0, 1, 2])
print(a[:1].shape)
print(a[:1, :2].shape)
print(a[:, :, 0:28:2, 0:28:2].shape)  # 0:28:2 表示从0到28每隔一个数据采样一次
print(a[:, :, ::2, ::2].shape)  # ::2每隔一个数据采样一次
print(a.index_select(1, torch.tensor([0, 2])).shape)  # 在第一个维度上选取0和2
print(a[...].shape)
print(a[..., :3].shape)

# 维度变换
a = torch.rand(4, 1, 28, 28)
print(a.shape)
print(a.view(4, 28 * 28))  # 将维度变成了4*784

# squeeze和unsqueeze（维度扩展）
a = torch.rand(4, 1, 28, 28)
print(a.unsqueeze(0).shape)  # 将维度变成了 1,4,1,28,28
print(a.unsqueeze(-1).shape)  # 将维度变成了 4,1,28,28,1

b = torch.rand(32)
f = torch.rand(4, 32, 14, 14)
b = b.unsqueeze(1).unsqueeze(2).unsqueeze(0)  # [1, 32, 1, 1]
print(b.shape)
print(b.squeeze().shape)  # [32]
print(b.squeeze(0).shape)  # [32, 1, 1]
print(b.squeeze(1).shape)  # [1, 32, 1, 1]

a = torch.rand(4, 32, 14, 14)
b = torch.rand(1, 32, 1, 1)
print(b.expand(4, 32, 14, 14).shape)  # expand仅仅只是扩展维度，而repeat是复制数据
print(a.repeat(4, 1, 1, 1).shape)  # 将第一个维度值乘以4

a = torch.rand(4, 3, 32, 32)
a1 = a.transpose(1, 3).contiguous().view(4, 3 * 32 * 32).view(4, 3, 32, 32)
a2 = a.transpose(1, 3).contiguous().view(4, 3 * 32 * 32).view(4, 32, 32, 3).transpose(1, 3)
print(torch.all(torch.eq(a, a1)))
print(torch.all(torch.eq(a, a2)))

print(a.permute(0, 2, 3, 1))  # 所有维度变换，一次到位
