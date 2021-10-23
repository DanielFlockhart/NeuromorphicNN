import math,random,string,Brain,Visualiser

if __name__ == "__main__":
    xvals=[]
    yvals=[]
    inputs = 1
    nodes = 4
    outputs = 1
    frames = 20
    brain = Brain.Brain(nodes,inputs,outputs)
    inputs = [0 for x in range(inputs)]
    for x in range(10000):
        brain.setInput(inputs)
        brain.normalise()
        xvals.append(inputs[0])
        yvals.append(brain.getValues()[0])
        inputs = [inputs[x] + random.uniform(-0.1,0.1) for x in range(len(inputs))]
    Visualiser.plotgraph(xvals,yvals)
    Visualiser.showgraph()