import math,random,string,Brain,time
from Visualiser import * 
from Controller import *


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
def encode_alpha(prompt):
    alpha =list(string.ascii_lowercase)
    res = [0 for x in range(10*26)]
    for x in range(len(prompt)):
        for z in range(26):
            res[x * 26 + z] = 1 if alpha.index(prompt[x]) == z else 0 
    return res

def decode_alpha(output):
    alpha =list(string.ascii_lowercase)
    
    prompt =["" for x in range(10)]
    for x in range(len(prompt)):
        part = output[x*26:x * 26 + 25]
        # causing the issue
        max_val = max(part)
        potential = [x if part[x] == max_val else 1000 for x in range(len(part))]
        max_index = 1000
        while max_index == 1000:
            max_index = random.choice(potential)
        
        #
        prompt[x] = alpha[max_index]
    return "".join(prompt)

def reverse_expand(x):
    return (x + 1) / 2
def convert(x,y):
    x = reverse_expand(x)
    y = reverse_expand(y)
    print(x)
    print(y)
    return (x * 2560,y * 1440)


def one_shot():
    (inp,nodes,out) = (3,2,3)
    brain = Brain.Brain(nodes,inp,out)
    #inputs = [1,0.8,0.5,-0.9,1]
    #prompt = "lmaooooooo"
    outputs = [1,1,1]
    for x in range(10000):
        input = [outputs[0],outputs[1],outputs[2]]
        #print(inp)
        process(brain,input)
        outputs = brain.getValues()
        res = convert(outputs[1],outputs[2])
        if(outputs[0] > 0):
            #click(res[0],res[1])
            print(res)
        #print(outputs)
        #prompt = decode(outputs)[-max(len(encode(prompt)),10):]
        #print(prompt)
        #display(brain)
        brain.gate()
        brain.learn(10,80,10)
    

        


if __name__ == "__main__":
    time.sleep(3)
    one_shot()
        