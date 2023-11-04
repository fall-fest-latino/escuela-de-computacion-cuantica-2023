## Challenge Statement

In this challenge, you will be provided with a variational quantum circuit in PennyLane that depends on a set of trainable parameters. The circuit outputs a single number as the expectation value of a fixed measurement. Your objective is to find the minimum expectation value this circuit can produce by optimizing its parameters. This will require converting the circuit into a QNode. You can either code up your own optimizer by calculating the gradient of the QNode, or you can use one of the provided PennyLane optimizers.

## Challenge code

The `variational_circuit` function contains the quantum circuit and has a `params` argument for specifying the trainable parameters. These are the parameters that need to be updated by the optimizer. Additionally, it has a `hamiltonian` argument, which specifies an unknown Hamiltonian that is used as an observable. The parameters describing the Hamiltonian are *not* trainable! 

You must fill in the `optimize_circuit` function so that it minimizes the variational circuit. It depends on the `hamiltonian` argument, which is the same as for `variational_circuit.` It is needed here since you are expected to call `variational_circuit` within this function.  In `optimize_circuit`, you will need to convert the variational circuit into an executable QNode using `qml.QNode()`.

In both functions, the Hamiltonian is specified by the problem input data, with each Hamiltonian resulting in a different minimum for the variational circuit. 

### Input

As input to this problem, you are given `hamiltonian` (`np.array(float)`), which is a list of parameters that encode the secret Hamiltonian whose expectation value is to be minimized.
 
### Output

The code will output a `float` corresponding to the minimum expectation value of the secret Hamiltonian, found by optimizing the input parameters in `variational_circuit.`

### Test cases

Here are some sample test cases for you to verify your code.

```python
test_input: [0.863327072347624,0.0167108057202516,0.07991447085492759,0.0854049026262154, 0.0167108057202516,0.8237963773906136,-0.07695947154193797,0.03131548733285282, 0.07991447085492759,-0.07695947154193795,0.8355417021014687,-0.11345916130631205, 0.08540490262621539,0.03131548733285283,-0.11345916130631205,0.758156886827099]
expected_output: 0.61745341

test_input: [0.32158897156285354,-0.20689268438270836,0.12366748295758379,-0.11737425017261123,-0.20689268438270836,0.7747346055276305,-0.05159966365446514,0.08215539696259792,0.12366748295758379,-0.05159966365446514,0.5769050487087416,0.3853362904758938,-0.11737425017261123,0.08215539696259792,0.3853362904758938,0.3986256655167206]
expected_output: 0.00246488
```

Good luck!