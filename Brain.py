

import math
from Node import *

class Brain():
    def __init__(self,nodes,inputs,outputs):
        self.nodes = self.build_nodes(nodes,inputs,outputs)
        self.setConnections()
        #self.outputs = [Output() for x in range(outputs))]

    def build_nodes(self,nodes,inputs,outputs):
        node_list = []
        id = 0
        for x in range(inputs):
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

        n0.connections = [(n1,0.2)]
        n1.connections = [(n3,-0.4),(n2,0.3)]
        n2.connections = []
        n3.connections = [(n2,-0.1)]

        return [n0,n1,n2,n3]

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
        

    def getValues(self):
        vals = []
        for node in self.nodes:
            if (node.type == "output"):
                vals.append(float("{:.4f}".format(node.activation)))
        return vals

    def normalise(self):
        for node in self.nodes:
            if node.activation > 1:
                node.activation = 1
            if node.activation < -1:
                node.activation = -1

        
    def setConnections(self):
        stretch = len(self.nodes) ** 2 - len(self.nodes)
        while stretch > 0:
            for node in self.nodes:
                choice = random.choice(self.nodes)
                # if choice is not itself, an input, already in its own connections or in the chosen nodes connectiosn then set as a connection
                if choice not in [node.connections[x][0] for x in range(len(node.connections))] and node not in [choice.connections[x][0] for x in range(len(choice.connections))] and choice.type != "input" and choice != node:
                    node.connections.append((choice,random.uniform(-1.0,1.0)))
                stretch -= 1

    def getConnections(self):
        print(self.nodes)
        for node in self.nodes:
            print([node.connections[x][0].id for x in range(len(node.connections))])

    def addNode(self,type):
        newNode = Neuron(len(self.nodes))
        self.nodes.append(newNode)
        self.rewire(newNode)

    def rewire(self,node):
        for z in range(5):
            choice = random.choice(self.nodes)
            if choice not in [node.connections[x][0] for x in range(len(node.connections))] and node not in [choice.connections[x][0] for x in range(len(choice.connections))] and choice.type != "input" and choice != node:
                node.connections.append((choice,random.uniform(-1.0,1.0)))
        for z in range(5):
            choice = random.choice(self.nodes)
            if choice not in [node.connections[x][0] for x in range(len(node.connections))] and node not in [choice.connections[x][0] for x in range(len(choice.connections))] and choice.type != "input" and choice != node:
                choice.connections.append((node,random.uniform(-1.0,1.0)))


            

    def backProp(self,node,step,lr):
        # Max step = how many synpases back it updates
        for PNode in self.nodes:
            if(node in [n[0] for n in PNodes.connection]):
                PNode.updatev.append(())
        pass