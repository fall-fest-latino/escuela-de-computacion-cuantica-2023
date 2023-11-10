### DO NOT CHANGE ANYTHING BELOW THIS LINE

import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm

WIRES = 2       #Numero de qubits
LAYERS = 5      #capas para el entrelazamiento de los qubits 
NUM_PARAMETERS = LAYERS * WIRES * 3   #Numero de parametros mejorables (30)

def variational_circuit(params,hamiltonian):
    """
    Esta es una plantilla de circuito cuántico variacional que contiene una composición fija de puertas con parámetros variables. Para ser utilizado como un QNode, debe ser envuelto con el decorador qml.qnode o convertido utilizando la función qml.QNode.
    La salida de este circuito es el valor de expectativa de un Hamiltoniano, codificado de alguna manera en el argumento hamiltoniano

    Args:
        - params(np.ndarray): Un array de parámetros optimizables de forma (30,)
        - hamiltonian(np.ndarray): Una matriz de parámetros reales que codifican el hamiltoniano cuyo valor de expectativa se devuelve.

    Return:
        (float): El valor de la expectativa del Hamiltoniano
    """
    parameters = params.reshape((LAYERS, WIRES, 3)) # lo transforma en una matriz 3D con dimensiones (LAYERS, WIRES, 3) y crea un circuito cuántico
    qml.templates.StronglyEntanglingLayers(parameters, wires=range(WIRES))    #que construye una serie de capas en las que cada qubit está entrelazado con sus vecinos. Los parámetros que se pasan (parameters) son los pesos del circuito variacional. 
    return qml.expval(qml.Hermitian(hamiltonian, wires = [0,1]))              #Se evalúa el valor esperado de un operador hermitiano (hamiltoniano). 

def optimize_circuit(hamiltonian):
    """Minimiza el circuito variacional y devuelve su valor mínimo.
    Debes crear un dispositivo y convertir la función variational_circuit en un QNode ejecutable.
    A continuación, debes minimizar el circuito variacional utilizando la optimización basada en el gradiente para actualizar los parámetros de entrada.
    Devuelve el valor optimizado del QNode como un único número en coma flotante.

    Args:
        - params (np.ndarray): Parámetros de entrada a optimizar, de dimensión 30
        - hamiltonian (np.ndarray): Un array de parámetros reales que codifican el Hamiltoniano cuyo valor de expectativa debe minimizar.
    Devuelve:
        float: el valor del QNode optimizado
    """

    hamiltonian = np.array(hamiltonian, requires_grad = False) #Esta línea convierte la variable hamiltoniana en una matriz NumPy y establece requires_grad en False.

    hamiltonian = np.array(hamiltonian,float).reshape((2 ** WIRES), (2 ** WIRES)) 

    ### WRITE YOUR CODE BELOW THIS LINE

    ### Solution Template

    dev = qml.device('default.qubit', wires = WIRES)        #Crea un simulador básico para cálculos cuánticos basados en qubits. El parámetro wires especifica el número de qubits de la simulación.
    nums = qml.numpy.random.rand(NUM_PARAMETERS)            #Genera una matriz de números aleatorios.

    @qml.qnode(dev)               # Se utiliza para convertir la función de coste en un QNode de PennyLane. En PennyLane, un QNode representa un nodo cuántico, o una función cuántica que puede evaluarse mediante un dispositivo cuántico.
    def cost(x):
      return variational_circuit(x, hamiltonian)      # A continuación, este QNode puede utilizarse para evaluar la función de coste, lo que normalmente implica ejecutar el circuito cuántico, medir algunos observables y calcular un valor de coste o expectativa basado en los resultados.
                                                      # Este es un paso crucial en los algoritmos cuánticos variacionales, en los que la optimización de los parámetros se realiza minimizando la función de coste.


    opt=qml.GradientDescentOptimizer(stepsize = 0.5)      #Escogemos un optimizador (definido en pennylane), en este caso el gradiente. Le damos un tamaño de paso de 0.5 
    steps = 100       

    params = nums    

    for i in tqdm(range(steps)):   
      params = opt.step(cost, params)   # El optimizador es probablemente un método de optimización basado en gradiente, como el descenso de gradiente estocástico (SGD) o una variante del mismo. Esta línea realiza esencialmente un paso de optimización.
      if (i + 1) % 10 == 0:       # 
            print("Cost after step {:5d}: {: .8f}".format(i + 1, cost(params)))

    # Write your code to minimize the circuit

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

optimize_circuit(in1)

optimize_circuit(in2)
