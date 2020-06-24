import torch
from torch.nn import functional as F

x = torch.randn(1, 784)
w = torch.randn(10, 784)

logits = x @ w.t()
pred = F.softmax(logits, dim=1)
pred_log = torch.log(pred)
print(F.nll_loss(pred_log, torch.tensor([3])))
print(F.cross_entropy(logits, torch.tensor([3])))
# cross_entropy 相当于先softmax操作，再log操作，最后进行nll_loss操作