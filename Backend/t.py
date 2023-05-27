import torch
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(torch_device)