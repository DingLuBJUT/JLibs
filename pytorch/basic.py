import torch

"""  ** get data device type and data type **   """
print("""** get data device type and data type **""")
data = torch.randn(2,3)
device_type, data_type = data.device, data.dtype
print(device_type, data_type)
print()

""" ** view, reshape, permute ** """
print("""** view, reshape, permute **""")
data = torch.randn(2,3)
# reshape data and data must has continue address space
print(data.view(3,2))
# exchange data dim and will break continue address space
print(data.permute(1, 0))
# reshape data
print(data.reshape(3,2))
print()

""" ** numel ** """
print("""** numel **""")
data = torch.randn(2, 3)
# get element num in tensor
print(data.numel())
print()

""" ** expand tensor dim ** """
print("""** expand tensor dim **""")
data = torch.randn(2, 3)
# torch.Size([1, 2, 3])
print(data[None,:].size(), data.unsqueeze(0).size())
# torch.Size([2, 1, 3])
print(data[:,None].size(), data.unsqueeze(1).size())
# torch.Size([2, 1, 3])
print(data[:,None,:].size(), data.unsqueeze(2).size())
print()

""" ** expand tensor data ** """
print("""** expand tensor data **""")
data = torch.randn(1, 3)
# expand data in first dim
print(data.expand(4, 3))
print(data.expand_as(torch.randn(4, 3)))
print()

""" ** clamp ** """
print("""** clamp **""")
data = torch.randn(3, 3)
# if less min return 0, if more than max return 1, else return self data
print(data.clamp(min=0, max=1))
print()

""" ** to ** """
print("""** to **""")
device = 'cuda' if torch.cuda.is_available() else 'cpu'
# to use special tensor data type and data device
data.to(torch.randn(size=(1,2), dtype=torch.float32, device=device))
print()

""" ** full ** """
print("""** full **""")
# fill special data with size
print(torch.full((3,), 0))
print(torch.full((3,3), 0))
print()

""" ** split ** """
print("""** split **""")
# split data with size in special dim
data = torch.randn(size=(5,3))
# split data, return (2,3)、(2,3)、(1,3)
print(torch.split(data, 2, dim=0))
# split data, return (2,3)、(3,3)
print(torch.split(data, [2, 3], dim=0))
print()

""" ** max max(dim) ** """
print("""** max max(dim) **""")
data = torch.randn(size=(5,3))
# return max value in data
print(data.max())
# return max value and max index in dim
# values = tensor([1.3650, 0.9711, 2.1888])
# indices = tensor([2, 2, 3]))
value, index = data.max(dim=0)
print()

""" ** ge、le、gt、lt、logical_and ** """
print("""** ge、le、gt、lt、logical_and **""")
data = torch.randn(size=(5,3))
# data >= 1, data <= 1, data > 1, data < 1, return Boolean Tensor
print(data.ge(1))
# data >= 1 and data <= 1, return Boolean Tensor
print(torch.logical_and(data.ge(1),data.le(4)))
print()

""" ** where ** """
print("""** where **""")
data = torch.randn(size=(5,3))
# if condition is True return first else return two
print(torch.where(data > 0.0, 1.0, -1.0))
# return True position
row_index, col_index = torch.where(data > 0.0)
print(row_index, col_index)
print()

""" ** meshgrid ** """
print("""** meshgrid **""")
x = torch.arange(3)
y = torch.arange(3)
# get coordinate system, return x coordinates and y coordinates
x, y = torch.meshgrid(x, y)
x, y = x.flatten(), y.flatten()
print(x, y)
print()

""" ** clone、detach ** """
print("""** clone、detach **""")
data = torch.randn(size=(5,3))
# clone data will push grad to data but not synchronization with data
c_data = data.clone()
# detach data will away from grad graph and synchronization with data
# even if address id is different, but synchronization with data
d_data = data.detach()
print()

""" ** topk ** """
print("""** topk **""")
data = torch.randn(size=(2,5))
# return max two value and two index in every row.
top_value,top_index = data.topk(2, dim=1)
# values = tensor([[1.6794, 0.3546], [1.0959, 0.3598]]),
# indices = tensor([[3, 1], [0, 1]]))
print(top_value, top_index)
print()

