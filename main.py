import math,random,string,Brain,time
from Visualiser import * 
from Controller import *


def getmax(li):
    random.shuffle(li)
    return li.index(max(li))
def display(brain):
    net = NetVisuals((500,500))
    net.build(brain.nodes)
    net.render()

def process(brain,input):
    brain.setInput(input)
    brain.normalise()
    return brain.getValues()

def calc_loss(results,expected):
    return sum([abs(results[x]-expected[x]) for x in range(len(expected))])

def reverse_expand(x):
    return (x + 1) / 2

def convert(x,y):
    x = reverse_expand(x)
    y = reverse_expand(y)
    return (x * 2560,y * 1440)

def encode_outputs(outputs):
    clickpos = convert(outputs[1],outputs[2])
    if(outputs[0] > 0):
        click(clickpos[0],clickpos[1])
    press_key(getmax(outputs[3:]))


def one_shot():
    (inp,nodes,out) = (3 + 26,20,3 + 26)
    brain = Brain.Brain(nodes,inp,out)
    outputs = [1 for x in range(inp)]
    while True:
        print("running")
        for x in range(1000):
            ins = outputs
            process(brain,ins)
            outputs = brain.getValues()
            encode_outputs(outputs)
            brain.gate()
            brain.learn(10,80,10)
        brain.sleep_nodes()
        print(brain.getConnections())
        display(brain)
    print("ended")

        


if __name__ == "__main__":
    time.sleep(3)
    one_shot()
        
