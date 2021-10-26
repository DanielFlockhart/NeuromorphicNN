import math,random,string,Brain
from Visualiser import * 


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

def one_shot():
    (inp,nodes,out) = (1,3,1)
    brain = Brain.Brain(nodes,inp,out)
    #inputs = [1,0.8,0.5,-0.9,1]
    inputs = [[1 for z in range(inp)] for x in range(100000)]
    exp = [1 for z in range(out)]

    for x in range(len(inputs)):
        process(brain,inputs[x])
    print(brain.getValues())
    display(brain)


if __name__ == "__main__":

    one_shot()