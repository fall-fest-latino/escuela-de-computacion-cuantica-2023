### DO NOT CHANGE ANYTHING BELOW THIS LINE

import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm

WIRES = 2
LAYERS = 5
NUM_PARAMETERS = LAYERS * WIRES * 3

def variational_circuit(params,hamiltonian):
    parameters = params.reshape((LAYERS, WIRES, 3))
    qml.templates.StronglyEntanglingLayers(parameters, wires=range(WIRES))
    return qml.expval(qml.Hermitian(hamiltonian, wires = [0,1]))
def optimize_circuit(hamiltonian):
    hamiltonian = np.array(hamiltonian, requires_grad = False)
    hamiltonian = np.array(hamiltonian,float).reshape((2 ** WIRES), (2 ** WIRES))

    ### WRITE YOUR CODE BELOW THIS LINE    
    ### Solution Template
    dev = qml.device("default.qubit", wires = WIRES)# Initialize the device.
    
    w = qml.numpy.random.rand(NUM_PARAMETERS)
#    qnod = qml.QNode(variational_circuit(w,hamiltonian),dev)
    @qml.qnode(dev)
    def cost(wei):
        return variational_circuit(wei,hamiltonian)
        
# Write your code to minimize the circuit
    opt=qml.GradientDescentOptimizer(stepsize=0.3)  
    
# set the number of steps
    steps = 160
    
# set the initial parameter values
    params = w

    for i in tqdm(range(steps)):
        # update the circuit parameters
        params = opt.step(cost, params)

        if (i + 1) % 10 == 0:
            print("Cost after step {:5d}: {: .8f}".format(i + 1, cost(params)))


in1=np.array([0.863327072347624,0.0167108057202516,0.07991447085492759,0.0854049026262154,
              0.0167108057202516,0.8237963773906136,-0.07695947154193797,0.03131548733285282,
              0.07991447085492759,-0.07695947154193795,0.8355417021014687,-0.11345916130631205,
              0.08540490262621539,0.03131548733285283,-0.11345916130631205,0.758156886827099])
#Expected output: 0.61745341
in2=np.array([0.32158897156285354,-0.20689268438270836,0.12366748295758379,-0.11737425017261123,
              -0.20689268438270836,0.7747346055276305,-0.05159966365446514,0.08215539696259792,
              0.12366748295758379,-0.05159966365446514,0.5769050487087416,0.3853362904758938,
              -0.11737425017261123,0.08215539696259792,0.3853362904758938,0.3986256655167206])
#Expected output: 0.00246488


#Run test cases
optimize_circuit(in1)

optimize_circuit(in2)
