import pennylane as qml
from pennylane import numpy as np
WIRES = 2
LAYERS = 5
NUM_PARAMETERS = LAYERS * WIRES * 3

def variational_circuit(params, hamiltonian):
    parameters = params.reshape((LAYERS, WIRES, 3))
    qml.templates.StronglyEntanglingLayers(parameters, wires=range(WIRES))
    return qml.expval(qml.Hermitian(hamiltonian, wires=[0, 1]))

def optimize_circuit(hamiltonian,stepsizee,num_stepss):
    hamiltonian = np.array(hamiltonian, requires_grad=False)
    hamiltonian = np.array(hamiltonian, float).reshape((2 ** WIRES), (2 ** WIRES))

    dev = qml.device('default.qubit', wires=WIRES)
    circuit = qml.QNode(variational_circuit, dev)
    init_params = np.random.randn(NUM_PARAMETERS)
    def cost(params):
        return circuit(params, hamiltonian)
    optimizer = qml.GradientDescentOptimizer(stepsize=0.4)
    num_steps = 200
    params = init_params
    for _ in range(num_steps):
        params = optimizer.step(cost, params)
    return cost(params)

if __name__ == "__main__":
    min_value = float('inf')
    best_stepsizee = None
    best_num_stepss = None
    hamiltonian_example = np.array(
        [0.32158897156285354,-0.20689268438270836,0.12366748295758379,-0.11737425017261123,
    -0.20689268438270836,0.7747346055276305,-0.05159966365446514,0.08215539696259792,
    0.12366748295758379,-0.05159966365446514,0.5769050487087416,0.3853362904758938,
    -0.11737425017261123,0.08215539696259792,0.3853362904758938,0.3986256655167206])
    for _ in range(1000):
        stepsizee = np.random.uniform(0.1,0.5)
        num_stepss = np.random.randint(100,500)
        optimized_value = optimize_circuit(hamiltonian_example,stepsizee,num_stepss)
        if optimized_value < min_value:
            min_value = optimized_value
            best_stepsizee = stepsizee
            best_num_stepss = num_stepss

    print("Optimized expectation value:", min_value)
    print("Best stepsize:", best_stepsizee)
    print("Best num_steps:", best_num_stepss)
