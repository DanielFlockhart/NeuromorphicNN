import Human
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
     
def fraw(vals):
    newVals = np.reshape(vals, (65536, 65536))
    print(newVals)
    plt.pcolormesh(newVals)
    plt.show()


if __name__ == "__main__":
    dims = (4294967296,4000000,4294967296)
    agent = Human.Human(dims)
    inputs = [0 for x in range(dims[2])]
    for x in range(10):
        inputs = agent.frame(inputs)
        agent.rewire(0.00001)
    fraw(inputs)
