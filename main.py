import math,random,string,Brain,time
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
def encode(prompt):
    alpha =list(string.ascii_lowercase)
    res = [0 for x in range(10*26)]
    for x in range(len(prompt)):
        for z in range(26):
            res[x * 26 + z] = 1 if alpha.index(prompt[x]) == z else 0 
    return res

def decode(output):
    alpha =list(string.ascii_lowercase)
    
    prompt =["" for x in range(10)]
    for x in range(len(prompt)):
        part = output[x*26:x * 26 + 25]
        # causing the issue
        max_val = max(part)
        max_index = part.index(max_val)
        #
        prompt[x] = alpha[max_index]
    return "".join(prompt)

def one_shot():
    (inp,nodes,out) = (26 * 10,2,26 * 10)
    brain = Brain.Brain(nodes,inp,out)
    #inputs = [1,0.8,0.5,-0.9,1]
    prompt = "lmaooooooo"
    for x in range(1000):
        inp = encode(prompt)
        #print(inp)
        process(brain,inp)
        outputs = brain.getValues()
        print(outputs)
        prompt = decode(outputs)[-max(len(encode(prompt)),10):]
        #print(prompt)
        #display(brain)
        brain.learn(10,80,10)
        if(prompt == "danksmemes"):
            print("found solution")
            localtime = time.asctime( time.localtime(time.time()) )
            print("Local current time :", localtime)
            return 100
    print("end of net")
    

        


if __name__ == "__main__":
    res = 0
    while res != 100:
        res = one_shot()
        