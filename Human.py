import math,random,string,Brain,time
from Visualiser import * 
from Controller import *


class Human:
    def __init__(self,dims):
        self.brain = Brain.Brain(*dims)

    def frame(self,inp):
        out = self.process(inp)
        self.brain.gate()
        return out

    def rewire(self,rate):
        self.brain.gate()
        if(rate > random.random()):
            self.brain.sleep_nodes()

    def process(self,input):
        self.brain.setInput(input)
        self.brain.normalise()
        return self.brain.getValues() 

    def display(self):
        net = NetVisuals((500,500))
        net.build(self.brain.nodes)
        net.render()

    def calc_loss(self,results,expected):
        return sum([abs(results[x]-expected[x]) for x in range(len(expected))])