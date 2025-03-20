import torch
import torch.nn as nn

#nn.Sequential
class NNBranch(nn.Module):  # 继承 nn.Module
    def __init__(self, paramsArr):
        super().__init__()
        self.a = nn.Linear(paramsArr['a'][0], paramsArr['a'][1])
        self.b = nn.Linear(paramsArr['b'][0], paramsArr['b'][1])
        self.c = nn.Linear(paramsArr['c'][0], paramsArr['c'][1])
        self.d = nn.Linear(paramsArr['d'][0], paramsArr['d'][1])
        self.relu = nn.ReLU()  # ReLU 作为类变量
        self.bn = nn.BatchNorm1d(paramsArr['a'][1])
    def forward(self, numArr):
        out = self.a(numArr)
        out = self.bn(out)

        out = self.relu(out)
        # self.bn(out)
        out = self.relu(self.b(out))
        out = self.relu(self.c(out))
        out = self.d(out)  # 最后一层通常不加 ReLU
        return out

if __name__ == "__main__":
    model = NNBranch({
        'a': [4096, 2048],
        'b': [2048, 1024],
        'c': [1024, 516],
        'd': [516, 10],
    })
    numArr = torch.rand((10, 4096))  # batch_size = 10, 输入维度 4096
    fina = model(numArr)
    print(fina)