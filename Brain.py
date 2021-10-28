

import math
from Node import *
lim = 0.1
class Brain():
    def __init__(self,nodes,inputs,outputs):
        print(nodes,inputs,outputs)
        self.nodes = self.build_nodes(nodes,inputs,outputs)
        self.setConnections(1)

    def build_nodes(self,nodes,input,outputs):
        node_list = []
        id = 0
        for x in range(input):
            node_list.append(Input(id))
            id+=1
        for x in range(nodes):
            node_list.append(Neuron(id))
            id+=1
        for x in range(outputs):
            node_list.append(Output(id))
            id+=1
        
        return node_list

    def setNodes(self):
        n0 = Input(0)
        n1 = Neuron(1)
        n2 = Neuron(2)
        n3 = Neuron(3)
        n4 = Output(4)

        n0.connections = [[n1,0.2]]
        n1.connections = [[n3,-0.4],[n2,0.3]]
        n2.connections = [[n4,0.5]]
        n3.connections = [[n2,-0.1]]
        return [n0,n1,n2,n3,n4]

    def setInput(self,inputs):
        inputs_nodes = [x for x in self.nodes if x.type == "input"]
        for x in range(len(inputs_nodes)):
            self.nodes[x].activation = inputs[x]
            self.nodes[x].tempState = inputs[x]
        self.propogate()

    def propogate(self):
        for node in self.nodes:
            node.propogate()

        for node in self.nodes:
            node.load_state()
            if node.type == ("node" or "output"):
                node.activation += node.bias
        

    def getValues(self):
        vals = []
        for node in self.nodes:
            if (node.type == "output"):
                vals.append(float("{:.4f}".format(node.activation)))
        return vals

    def getWeights(self):
        vals = []
        for node in self.nodes:
            vals.append(node.connections)
        return vals

    def normalise(self):
        for node in self.nodes:
            if node.activation > 1:
                node.activation = 1
            if node.activation < -1:
                node.activation = -1

    def setConnections(self,density):
        for node in self.nodes:
            choice = node
            while choice == node:
                choice = random.choice(self.nodes)
                choice = self.addConnection(node,choice)

    def getConnections(self):
        print(self.nodes)
        for node in self.nodes:
            print([node.connections[x][0].id for x in range(len(node.connections))])

    def addNode(self,type):
        newNode = Neuron(len(self.nodes))
        self.nodes.append(newNode)
        return newNode

    def addConnection(self,origin,destination):
        if origin not in [destination.connections[x][0] for x in range(len(destination.connections))] and destination not in [origin.connections[x][0] for x in range(len(origin.connections))] and origin != destination:
            origin.connections.append([destination,random.uniform(-lim,lim)])
            return destination
        return origin

    def getConnectBy(self,node):
        cons = []
        for n in self.nodes:
            if(node != n):
                for c in n.connections:
                    if node == c[0]:
                        cons.append(n)
        return cons

    def learn(self,nr,cr,iters):
        for x in range(iters):
            if random.randint(0,100) < nr:
                n = self.addNode("node")
                self.addConnection(n,random.choice(self.nodes))

            if random.randint(0,100) < cr:
                self.addConnection(random.choice(self.nodes),random.choice(self.nodes))
    def gate(self):
        for node in self.nodes:
            if((node.activation or node.tempState)== (1 or -1)):
                node.activation = 0
                node.tempState = 0
    # Distance backprop
    '''

    def getWeight(self,n1,n2):
        d = math.dist(n1.pos,n2.pos)
        return d * 2 if d < 0.5 else max(-(d - 0.5) * 2,-1)

    def update_weights(self):
        for (index,node) in enumerate(self.nodes):
            if (node.pullvector != [0,0]):
                #print(node.pullvector)
                pass
            node.pos[0] += node.pullvector[0] / len(node.connections)
            node.pos[1] += node.pullvector[1] / len(node.connections)
            for (i,c) in enumerate(node.connections):
                c[1] = self.getWeight(node,c[0])

    

    def fullBackprop(self,expected):
        pointer = 0
        for node in self.nodes:
            if (node.type == "output"):
                loss = node.activation - expected[pointer]
                self.backProp(node,5,0.003,loss)
                pointer+=1
        self.update_weights()
        
    def backProp(self,node,step,lr,loss):
        # Max step = how many synpases back it updates
        # Recurrisive is best option
        cons = self.getConnectBy(node)
        if step == 0 or len(cons) == 0 or node.type == "input":
            return
        for (index,c) in enumerate(cons):
            
            dX = (c.pos[0]-node.pos[0]) if abs(c.pos[0]-node.pos[0]) <= 1 else 0
            dY = (c.pos[1]-node.pos[1]) if abs(c.pos[1]-node.pos[1]) <= 1 else 0
            if dX > 2:
                print(dX)
            c.pullvector[0] -= dX * lr
            c.pullvector[1] -= dY * lr
            self.backProp(c,step-1,lr,loss)
        return
    '''




    # weight backprop
    '''
    def rewire(self,node):
        for z in range(5):
            choice = random.choice(self.nodes)
            if choice not in [node.connections[x][0] for x in range(len(node.connections))] and node not in [choice.connections[x][0] for x in range(len(choice.connections))] and choice.type != "input" and choice != node:
                node.connections.append((choice,random.uniform(-1.0,1.0)))
        for z in range(5):
            choice = random.choice(self.nodes)
            if choice not in [node.connections[x][0] for x in range(len(node.connections))] and node not in [choice.connections[x][0] for x in range(len(choice.connections))] and choice.type != "input" and choice != node:
                choice.connections.append((node,random.uniform(-1.0,1.0)))


    def fullBackprop(self,expected):
        pointer = 0
        for node in self.nodes:
            if (node.type == "output"):
                loss = node.activation - expected[pointer]
                self.backProp(node,2,0.01,abs(loss))
                pointer+=1
        self.update_weights()
        
    def backProp(self,node,step,lr,loss):
        # Max step = how many synpases back it updates
        # Recurrisive is best option
        current_loss = loss
        cons = self.getConnectBy(node)
        if step == 0 or len(cons) == 0 or loss <= 0:
            return
        for (index,c) in enumerate(cons):
            node.updatev[index] = 0.01 * loss
            current_loss = loss - node.updatev[index]
            self.backProp(c,step-1,lr,current_loss)
        return
    '''