

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
    def setInput(self,inputs):
        inputs_nodes = [x for x in self.nodes if x.type == "input"]
        for x in range(len(inputs_nodes)):
            self.nodes[x].activation = inputs[x]
        self.propogate()

    def propogate(self):
        for node in self.nodes:
            node.propogate()
            

    def getValues(self):
        vals = []
        for node in self.nodes:
            if node.type == "output":
                vals.append(node.activation)
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
        for node in self.nodes:
            print([node.connections[x][0].id for x in range(len(node.connections))])


    def addNode(self,type):
        self.nodes.append(Neuron(len(self.nodes)))

    def rewire(self):
        stretch = len(self.nodes) * 2
        while stretch > 0:
            for node in self.nodes:
                choice = random.choice(self.nodes)
                # if choice is not itself, an input, already in its own connections or in the chosen nodes connectiosn then set as a connection
                if choice not in [node.connections[x][0] for x in range(len(node.connections))] and node not in [choice.connections[x][0] for x in range(len(choice.connections))] and choice.type != "input" and choice != node:
                    node.connections.append((choice,random.uniform(-1.0,1.0)))
                stretch -= 1


            


        