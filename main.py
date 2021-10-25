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


def one_shot():
    (inputs,nodes,outputs) = (2,4,3)
    brain = Brain.Brain(nodes,inputs,outputs)
    #inputs = [1,0.8,0.5,-0.9,1]
    inputs = [[random.uniform(-1.0,1.0) for z in range(inputs)] for x in range(random.randint(10,100))]
    outputs = []
    for x in range(len(inputs)):
        process(brain,inputs[x])
        brain.backProp()
    display(brain)


if __name__ == "__main__":

    one_shot()