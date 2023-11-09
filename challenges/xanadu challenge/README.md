
# Quantum Circuit Optimizer with PennyLane

This project implements a variational quantum circuit optimizer using the PennyLane
quantum computing library. The goal is to minimize the expected value of a fixed
measurement by adjusting the parameters of a variational quantum circuit, which represents
a QNode in PennyLane. This optimization process is crucial for tasks such as quantum state
preparation and solving energy problems in physical systems modeled by specific
Hamiltonians.

The project demonstrates how to convert a quantum circuit into an executable QNode and how to apply optimizers to find the parameters that result in the minimum expected value of an unknown observable. Concrete examples are provided, and the effectiveness of the optimizer is shown using different Hamiltonians as test cases.




## Installation

Install Pennylane

To install PennyLane and run the quantum circuit optimizer, follow these steps:

- Ensure you have Python installed on your system.
- Install PennyLane using pip with the following command:

```bash
  pip install pennylane
```
    
## Dependencies

**PennyLane:** A Python library that simplifies the simulation and optimization of quantum circuits. It is the only dependency required to run this project.




## Usage

To use the code, you need to download the Pennylane_Challenge.ipynb file, meet the dependencies (Python and Pennylane), and start running the project step by step from top to bottom.

To test different Hamiltonians, simply modify the line of code:

```bash
  hamiltonian_example = np.array(
  [0.32158897156285354,-0.20689268438270836,0.12366748295758379,-0.11737425017261123,
  -0.20689268438270836,0.7747346055276305,-0.05159966365446514,0.08215539696259792,
  0.12366748295758379,-0.05159966365446514,0.5769050487087416,0.3853362904758938,
  -0.11737425017261123,0.08215539696259792,0.3853362904758938,0.3986256655167206])
```

Pennylane examples:

```bash
    [0.863327072347624,0.0167108057202516,0.07991447085492759,0.0854049026262154,
    0.0167108057202516,0.8237963773906136,-0.07695947154193797,0.03131548733285282,
    0.07991447085492759,-0.07695947154193795,0.8355417021014687,-0.11345916130631205,
    0.08540490262621539,0.03131548733285283,-0.11345916130631205,0.758156886827099]
```
- expected_output: `0.61745341`
```bash
    [0.32158897156285354,-0.20689268438270836,0.12366748295758379,-0.11737425017261123,
    -0.20689268438270836,0.7747346055276305,-0.05159966365446514,0.08215539696259792,
    0.12366748295758379,-0.05159966365446514,0.5769050487087416,0.3853362904758938,
    -0.11737425017261123,0.08215539696259792,0.3853362904758938,0.3986256655167206]
```
- expected_output: `0.00246488`

## Physic context of the problem


Let $\hat{H}$ be a hamiltonian in a quantum Hilbert space $\mathcal{H}$, then for its ground state:


<p align="center">
	$\hat{H} \ket{\Psi_0} = E_0 \ket{\Psi _0}$
</p>

with $E_0$ its eigenvalue, then the expected value:

<p align="center">
$\braket{H}_{\Psi_0} = \bra {\Psi _0} \hat{H} \ket{\Psi_0} =E_0\braket{\Psi |  \Psi}   = E_0$
</p>


For an arbitrary $\ket{\Psi} \in \mathcal{H}$, it can be showed:


<p align="center">
$\bra{\Psi _0} \hat{H} \ket{\Psi_0} \leq \bra{\Psi} \hat{H} \ket{\Psi} \Rightarrow \braket{H}_{\Psi_0} \leq   \braket{H}_{\Psi}$
</p>

Given $\hat{H}$, if we want to obtain the ground state we can propouse a parametrized state (an ansatz):


<p align="center">
	$\ket{\Psi (θ)} = \hat{W}_\theta \ket{0}^{\otimes n}$
</p>


and so we can attempt to find the parameters that characterize the ground state:


<p align="center">
$\ket{\Psi_0} = \hat{W}_θ \ket{0}^{\otimes n}$
</p>


then ,due the expected value of the hamiltonian in the ground states is less or equal to the expected value for an  arbitrary state, for  the ground state we must  find  the parameters of the operator     $\hat{W}$(θ)    that minimize the expected value for the Hamiltonian  $\hat{H}$  in    $\hat{W}$(θ) $\ket{0}^{\otimes n}$  , i,e   $\braket{H}$ $_{\Psi(θ)}$


We can encode our minimization problem of a cost function, the expected value, with a Variational Quantum Algorithm and  use tools like PennyLane! 

## Screenshots and Code explanation

For the development of this code, we started with the template provided by PennyLane. The only necessary library is PennyLane, and initially, we begin with the definition of what will be our number of wires or qubits, our number of layers in the circuit, and our total number of parameters.

![App Screenshot](https://arnoldodany.com/QCImages/QC_librer%C3%ADas.png)

The function "variational_circuit" aims to construct a variational quantum circuit (VQC), which is a type of parameterized quantum circuit frequently used in quantum algorithms, especially in the fields of quantum optimization and quantum machine learning.

Parameter Reshaping: The function starts by taking an argument called params, which is an array of numerical values. These values are the variational parameters that will control certain quantum operations (gates) in the circuit. The params array is reshaped to match the number of layers (LAYERS) and the number of qubits (WIRES) in the circuit. Each qubit in each layer will have three associated parameters.

Construction of Entangling Layers: It uses a template called StronglyEntanglingLayers from the quantum computing library. This template applies a series of quantum gates that strongly entangle the qubits, thereby creating quantum entanglement between them. Entanglement is a key resource in quantum computing that allows qubits to be correlated in a way that is not possible in classical systems.

StronglyEntanglingLayers: StronglyEntanglingLayers is one of the templates provided by PennyLane. This template creates a sequence of layers where each layer consists of single-qubit rotation gates and two-qubit entangling gates. The single-qubit rotations are typically applied to each qubit and are parametrized by the input parameters. The two-qubit entangling gates are CNOTs or other entangling gates that link the qubits together, creating quantum entanglement between them.

![App Screenshot](https://arnoldodany.com/QCImages/StronglyCircuit.png)

Expectation Value Evaluation: Finally, the function calculates the expected value of a given Hamiltonian operator (hamiltonian). In quantum mechanics, the expectation value of a Hamiltonian with respect to a quantum state gives the average energy of that state. In this case, the Hamiltonian is applied to the first two qubits of the circuit. The expected value is a critical measure in VQCs, as it is often sought to minimize this value through a variational optimization process, by adjusting the circuit parameters to find the state of lowest energy, which is the optimal solution to the problem at hand.

![App Screenshot](https://arnoldodany.com/QCImages/QC_circuito.png)

This code defines a function named optimize_circuit that aims to optimize a variational quantum circuit given a Hamiltonian. Here's a breakdown of the function and the rationale behind each part:

Hamiltonian Conversion: The function starts by converting the hamiltonian input into a NumPy array and ensuring that it does not require a gradient. This is necessary because the optimization process involves computing gradients, and the Hamiltonian's own gradient is not relevant to this process.

Hamiltonian Reshaping: The Hamiltonian is reshaped into a square matrix of size 4x4, which is suitable for a system with two qubits (since $2^2$ = 4). This is because the Hamiltonian must be a matrix where the dimensions are equal to the number of possible states of the system.

Quantum Device Definition: A quantum device is instantiated using PennyLane's default.qubit simulator, setting the number of wires (qubits) it will use. This device will simulate the quantum circuit.

Quantum Node Creation: A quantum node (QNode) is created with the variational_circuit function previously discussed, and the quantum device dev. A QNode wraps a quantum function (the circuit) for execution on a specific device.

Parameter Initialization: The circuit parameters are initialized to random values. This is a common practice in optimization, as starting from different random points can help in avoiding local minima and finding a better global solution.

Cost Function: The cost function is defined to be the expected value of the Hamiltonian, which is what we seek to minimize. It uses the circuit to compute this expected value given the current parameters.

Optimizer Definition: A gradient descent optimizer is initialized with a specified step size. Gradient descent is an optimization algorithm that iteratively adjusts parameters to minimize the cost function.

Optimization Loop: The optimization process is carried out for a predefined number of steps (num_steps). In each step, the optimizer adjusts the parameters to minimize the cost function.

Return Optimized Cost: After the optimization loop, the function returns the optimized cost, which is the lowest expected value of the Hamiltonian found by the optimization process.

![App Screenshot](https://arnoldodany.com/QCImages/QC_funcion.png)

min_value Initialization: The variable min_value is initialized to float('inf'), which is a way of setting it to "infinity" in Python. This value serves as a comparison baseline for finding the minimum expectation value as the optimization proceeds.

Hamiltonian Definition: hamiltonian_example is defined as a NumPy array representing a Hamiltonian, which is a matrix associated with the total energy of the quantum system. In quantum computing, we often seek to find the ground state (the state of lowest energy) of such a system.

Optimization Call: The optimize_circuit function is called with the defined Hamiltonian. Although the function itself is not shown in the snippet, we can infer that it involves setting up a variational quantum circuit, initializing parameters, defining a cost function (usually the expectation value of the Hamiltonian), and using an optimizer to adjust the parameters to minimize the cost.

Print Optimized Value: After the optimization routine completes, the optimized expectation value (presumably the lowest found by the optimizer) is printed out. This value represents the energy of the system in the state dictated by the optimized parameters of the variational quantum circuit.

![App Screenshot](https://arnoldodany.com/QCImages/QC_maini.png)
## Test cases

For this project, two Hamiltonians provided by PennyLane were used to verify the code's functionality.

- input: 
```bash
    [0.863327072347624,0.0167108057202516,0.07991447085492759,0.0854049026262154,
    0.0167108057202516,0.8237963773906136,-0.07695947154193797,0.03131548733285282,
    0.07991447085492759,-0.07695947154193795,0.8355417021014687,-0.11345916130631205,
    0.08540490262621539,0.03131548733285283,-0.11345916130631205,0.758156886827099]
```
- expected_output: `0.61745341`
- proyect_output: `0.6174534088312781`

- input: 
```bash
    [0.32158897156285354,-0.20689268438270836,0.12366748295758379,-0.11737425017261123,
    -0.20689268438270836,0.7747346055276305,-0.05159966365446514,0.08215539696259792,
    0.12366748295758379,-0.05159966365446514,0.5769050487087416,0.3853362904758938,
    -0.11737425017261123,0.08215539696259792,0.3853362904758938,0.3986256655167206]
```
- expected_output: `0.00246488`
- proyect_output: `0.0024648812008860755`


## Authors

#### Quantum Codebreakers

- [@Arnoldo Valdez](https://www.github.com/arnoldodany44)
- [@Alejandro Monroy](https://www.github.com/AzpMon)
- [@Francisco Costa](https://www.github.com/podxboq)
- [@Sofía Salazar](https://www.github.com/nsalazard)
- [@Julio Moreno](https://www.github.com/pyspdev)

