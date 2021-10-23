import math,random,string,Brain,Visualiser


def one_shot(frames,input,target = 0.3):

    #xvals=[]
    #yvals=[]
    inputs = 1
    nodes = 4
    outputs = 1
    loss = 0
    brain = Brain.Brain(nodes,inputs,outputs)
    inputs = [-2]#[0 for x in range(inputs)]
    # DOING DEPTH FIRST INSTEAD OF BREADTH FIRST
    for x in range(frames):
        brain.setInput(inputs)
        brain.normalise()
        #xvals.append(inputs[0])
        #yvals.append(brain.getValues()[0])
        inputs = [inputs[x] + random.uniform(-0.1,0.1) for x in range(len(inputs))]
        loss += abs((0.3 - brain.getValues()[0])/target)

        #if(x % 1000 == 0):
        #   brain.addNode("node")
    return loss
    #Visualiser.plotgraph(xvals,yvals)
    #Visualiser.showgraph()


if __name__ == "__main__":
    frames = 100000
    accuracy = []
    bestAccuracy = one_shot(frames=1000,input=-2)
    for x in range(frames):
        loss = one_shot(frames=1000,input=-2)
        if loss < bestAccuracy:
            bestAccuracy = loss
            print(bestAccuracy)
        accuracy.append(bestAccuracy)
    Visualiser.plotgraph([x for x in range(len(accuracy))],accuracy)
    Visualiser.showgraph()