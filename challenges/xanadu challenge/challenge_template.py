### DO NOT CHANGE ANYTHING BELOW THIS LINE

import pennylane as qml
from pennylane import numpy as np

import matplotlib.pyplot as plt
#plt.style.use(['science', 'no-latex'])

WIRES = 2
LAYERS = 5
NUM_PARAMETERS = LAYERS * WIRES * 3

def variational_circuit(params,hamiltonian):
    parameters = params.reshape((LAYERS, WIRES, 3))
    qml.templates.StronglyEntanglingLayers(parameters, wires=range(WIRES))
    return qml.expval(qml.Hermitian(hamiltonian, wires = [0,1]))

def optimize_circuit(hamiltonian, stepsize=85, momentum=0.62, ch_opt="Grad", steps=400, traceback=False):

    hamiltonian = np.array(hamiltonian, requires_grad = False)
    hamiltonian = np.array(hamiltonian,float).reshape((2 ** WIRES), (2 ** WIRES))

    ### WRITE YOUR CODE BELOW THIS LINE

    #Hamiltonian    = Data
    #stepsize       = Stepsize
    #momentum       = Momentum
    #ch_opt         = Optimizer
    #Min            = Expected output
    
    dev = qml.device("default.qubit", wires = WIRES)

    w = qml.numpy.random.rand(NUM_PARAMETERS)
    @qml.qnode(dev)
    
    def cost(wei):
        return variational_circuit(wei,hamiltonian)

    if ch_opt== "Momentum":
        opt=qml.MomentumOptimizer(stepsize=stepsize, momentum=momentum)
    elif ch_opt== "Adagrad":
        opt=qml.AdagradOptimizer(stepsize=stepsize)
    elif ch_opt=="Grad":
        opt=qml.GradientDescentOptimizer(stepsize=stepsize)

    params = w
    p_cost = cost(params)

    for i in range(steps):
        
        params = opt.step(cost, params)
        a_cost = cost(params)

        if (abs(p_cost - a_cost)) < 5*1e-9:
            break

        if (i+1) % 10 == 0 and traceback:
            print('Step_size {}: Cost: {:.8f}'.format(i, cost(params)))

        p_cost = a_cost
        
    
    if traceback:
        print('Final cost: {:.8f}'.format(cost(params)))

    return cost(params)
        
    

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

# Test Cases
a = optimize_circuit(in1, ch_opt="Momentum", traceback=True)
print(a)
b = optimize_circuit(in2, ch_opt="Momentum", traceback=True)
print(b)

"""
# ADAGRAD

steps = np.linspace(0.1, 0.15, 20)

iterations_1 = []
iterations_2 = []

for step in steps:
  i_1 = optimize_circuit(hamiltonian=in1, stepsize=step,ch_opt="Adagrad")
  i_2 = optimize_circuit(hamiltonian=in2, stepsize=step,ch_opt="Adagrad")
  iterations_1.append(i_1)
  iterations_2.append(i_2)

#Figure
fig = plt.figure(figsize=(6,5))
plt.plot(steps, iterations_1, 'b.',label='Test Input 1')
plt.plot(steps, iterations_2, 'g.',label='Test Input 2')
plt.legend(loc='upper left')
plt.xlabel('Step Size', fontsize = 12)
plt.ylabel('Steps', fontsize = 12)
plt.title('Steps to Converge vs Stepsize AdagradOptimizer');
#plt.savefig('grafica.png')

# GRADIENT DESCENT

steps = np.linspace(0.1, 1, 20)
iterations = []

for step in steps:
  i = optimize_circuit(hamiltonian=in1, stepsize=step,ch_opt="Grad")
  iterations.append(i)

fig = plt.figure(figsize=(5,4))
plt.plot(steps, iterations, 'k.')
plt.xlabel('Step Size', fontsize = 12)
plt.ylabel('Steps', fontsize = 12)
plt.title('Steps to Converge vs Stepsize Gradient Descendent');

# MOMENTUM

steps = np.linspace(5e-1, 1, 20)
momentum = np.linspace(0.1, 1, 20)
iterations = []
aux = []

for step in steps:
  for mom in momentum:
    i = optimize_circuit(hamiltonian=in1, stepsize=step, momentum=mom,ch_opt="Momentum")
    aux.append(i)
  iterations.append(aux)
  aux = []

filtered_iterations = [np.array(aux[:-1]) if aux[-1] is None else np.array(aux) for aux in iterations]

args_min = []

for i in range(len(filtered_iterations)):
  j = np.argmin(filtered_iterations[:][i])
  args_min.append(j)

mins = []

for i in args_min:
    mins.append(filtered_iterations[i][args_min[i]])

min_iterations = np.min(filtered_iterations, axis=1)

fig = plt.figure(figsize=(8, 6))

for i in range(len(steps)):
    plt.plot(steps[i], mins[i], 'k.')

    plt.text(steps[i], mins[i] - 0.12, f'{momentum[args_min[i]]:.2f}', fontsize=10, ha='center', va='top')


plt.xlabel('Step Size', fontsize=12)
plt.ylabel('Steps', fontsize=12)
plt.title('Steps to Converge vs MomentumOptimizer')
plt.plot(0.975, 22.2, 'r.')
plt.text(0.94, 22, '(Momentum)', fontsize=10, ha='left', va='top')
plt.legend(loc='lower right')
plt.show()
"""