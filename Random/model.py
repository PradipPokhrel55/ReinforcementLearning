import tensor
import tensor.nn as nn
import tensor.nn.F as F 
import random


class Linear_QNet(nn.Model):
    def __init__(self,input_state,hidden_state,output_state):
        super().__inti__()
        self.Linear1 = nn.Linear(input_state,hidden_state)
        self.linear2 = nn.Linear(hidden_state,output_state)

    def Forward(self,x):
        x= F.relu(self.Linear1(x))
        x=self.linear2(x)
        return x