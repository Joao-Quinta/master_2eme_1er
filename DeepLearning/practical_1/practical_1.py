import torch
import numpy
from time import perf_counter

# multiple views of a storage

x = torch.full((13, 13), 3)

index_1 = torch.tensor([0, 2, 5, 7, 10, 12])
x.index_fill_(1, index_1, 1)
x.index_fill_(0, index_1, 1)

index_2 = torch.tensor([1, 6, 11])
x.index_fill_(1, index_2, 2)
x.index_fill_(0, index_2, 2)

# print(x)

# eigen decomposition

x = torch.normal(0, 1, (20, 20)).float()
x_inv = torch.inverse(x)
diag_matrix = torch.diag(torch.arange(1, 21)).float()

res = torch.mm(torch.mm(x_inv, diag_matrix), x)
L, V = torch.linalg.eig(res)

# print(L)
# print(V)

# flops per second

x = torch.normal(0, 1, (5000, 5000)).float()
y = torch.normal(0, 1, (5000, 5000)).float()

t1_start = perf_counter()
z = torch.mm(x, y)
t1_stop = perf_counter()

number_multiplications = 5000 * 5000 * 5000
time_multiplications = t1_stop-t1_start
# print(number_multiplications/time_multiplications, "per second")

# playing with strides
