import random
'''

Base Class


'''
class Node:
    def __init__(self,id):
        self.type = ""
        self.id = id
        self.pos = self.setPos()
        self.connections = []
        
        self.activation = 0
        self.tempState = 0
        
        
        
        

    def setPos(self):
        return (random.uniform(0,1.0),random.uniform(0,1.0))

    def getPos(self):
        print(self.pos)
    
    def getType(self):
        print(self.type)

    def propogate(self):
        self.updatev = [0 for x in range(len(self.connections))]
        # This is does not breadfirst if multidirectional graph
        for connection in self.connections:
            connection[0].tempState += connection[1] * self.activation
    
    def load_state(self):
        self.activation = self.tempState
                
        


'''

Output neuron
- outputs are arbritary
'''
class Output(Node):
    def __init__(self,id):
        super().__init__(id)
        self.type = "output"
        
    
    def act(self):
        print("Output action")


'''

Input neuron
- inputs are chosen


'''

class Input(Node):
    def __init__(self,id):
        super().__init__(id)
        self.type = "input"
        
    
    def act(self):
        print("Input action")

'''

Neuron
- maths


'''

class Neuron(Node):
    def __init__(self,id):
        super().__init__(id)
        self.type = "node"
    
    def act(self):
        print("Neuron Action")
