from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, Aer
from qiskit.circuit.library import XGate


def setting_initial_configuration(board):
    """
    Initializes a quantum circuit with the given Tic Tac Toe board configuration.

    Args:
        board (list of lists): Represents the Tic Tac Toe board.

    Returns:
        QuantumCircuit: Quantum circuit with the specified initial configuration.
    """
    n_qubits = 9
    counter_aux_qubits = 4
    aux_conditions_qubits = 8
    oracle_qubit = 1
    empty_spaces = sum(row.count(' ') for row in board)

    qreg_q = QuantumRegister(
        n_qubits + counter_aux_qubits + aux_conditions_qubits + oracle_qubit, 'q')

    creg_c = ClassicalRegister(empty_spaces, 'c')

    qc = QuantumCircuit(qreg_q, creg_c)

    counter = 0
    for row in board:
        for elem in row:
            if elem == 'O':
                qc.i(qreg_q[counter])
            elif elem == 'X':
                qc.x(qreg_q[counter])
            else:
                qc.h(qreg_q[counter])
            counter += 1

    return qc



def conditions_and_counter():
    """
    Creates a quantum circuit to apply conditions and count the number of 'X's on the board.

    Returns:
        QuantumCircuit: Quantum circuit for conditions and counting.
    """
    n_qubits = 9
    counter_aux_qubits = 4
    aux_conditions_qubits = 8
    oracle_qubit = 1

    qreg_q = QuantumRegister(
        n_qubits + counter_aux_qubits + aux_conditions_qubits + oracle_qubit, 'q')

    mcx = XGate().control(3)

    qc = QuantumCircuit(qreg_q)

    # 8 possible ways for 'X' to win the game
    qc.barrier()
    qc.mct([0, 3, 6], 13)
    qc.mct([0, 4, 8], 14)
    qc.mct([3, 4, 5], 15)
    qc.mct([1, 4, 7], 16)
    qc.mct([0, 1, 2], 17)
    qc.mct([2, 5, 8], 18)
    qc.mct([6, 7, 8], 19)
    qc.mct([2, 4, 6], 20)
    qc.barrier()

    # Bit adder, counting the number of 'X's on the board
    qc.cx(qreg_q[0], qreg_q[9])
    qc.barrier()

    qc.ccx(qreg_q[1], qreg_q[9], qreg_q[10])
    qc.cx(qreg_q[1], qreg_q[9])
    qc.barrier()

    qc.ccx(qreg_q[2], qreg_q[9], qreg_q[10])
    qc.cx(qreg_q[2], qreg_q[9])
    qc.barrier()

    qc.append(mcx, [3, 9, 10, 11])
    qc.ccx(qreg_q[3], qreg_q[9], qreg_q[10])
    qc.cx(qreg_q[3], qreg_q[9])
    qc.barrier()

    qc.append(mcx, [4, 9, 10, 11])
    qc.ccx(qreg_q[4], qreg_q[9], qreg_q[10])
    qc.cx(qreg_q[4], qreg_q[9])
    qc.barrier()

    qc.append(mcx, [5, 9, 10, 11])
    qc.ccx(qreg_q[5], qreg_q[9], qreg_q[10])
    qc.cx(qreg_q[5], qreg_q[9])
    qc.barrier()

    qc.append(mcx, [6, 9, 10, 11])
    qc.ccx(qreg_q[6], qreg_q[9], qreg_q[10])
    qc.cx(qreg_q[6], qreg_q[9])
    qc.barrier()

    qc.append(mcx, [7, 9, 10, 11])
    qc.ccx(qreg_q[7], qreg_q[9], qreg_q[10])
    qc.cx(qreg_q[7], qreg_q[9])
    qc.barrier()

    qc.append(mcx, [8, 9, 10, 11])
    qc.ccx(qreg_q[8], qreg_q[9], qreg_q[10])
    qc.cx(qreg_q[8], qreg_q[9])
    qc.barrier()

    qc.x(qreg_q[9])
    qc.x(qreg_q[10])

    qc.mct([9, 10, 11], 12)

    qc.barrier()

    return qc

def oracle():
    """
    Creates a quantum circuit for the oracle part of the algorithm.

    Returns:
        QuantumCircuit: Quantum circuit for the oracle.
    """
    n_qubits = 9
    counter_aux_qubits = 4
    aux_conditions_qubits = 8
    oracle_qubit = 1

    qreg_q = QuantumRegister(
        n_qubits + counter_aux_qubits + aux_conditions_qubits + oracle_qubit, 'q')

    qc = QuantumCircuit(qreg_q)

    qc = qc.compose(conditions_and_counter())

    qc.barrier()
    qc.x(21)
    qc.h(21)
    qc.barrier()

    # Oracle
    qc.mct([12, 13], 21)
    qc.mct([12, 14], 21)
    qc.mct([12, 15], 21)
    qc.mct([12, 16], 21)
    qc.mct([12, 17], 21)
    qc.mct([12, 18], 21)
    qc.mct([12, 19], 21)
    qc.mct([12, 20], 21)

    qc.barrier()
    qc = qc.compose(conditions_and_counter().inverse())

    return qc


def diffuser(board):
    """
    Creates a quantum circuit for the Grover Diffuser.

    Args:
        board (list): The Tic Tac Toe board.

    Returns:
        QuantumCircuit: Quantum circuit representing the Grover Diffuser.
    """
    n_qubits = 9
    one_dimensional_list = [value for row in board for value in row]
    index_empty_spaces = [i for i, value in enumerate(
        one_dimensional_list) if value == ' ']

    qreg_q = QuantumRegister(n_qubits, 'q')

    qc = QuantumCircuit(qreg_q)

    for qubit in index_empty_spaces:
        qc.h(qubit)
    # Apply transformation |00..0> -> |11..1> (X-gates)
    for qubit in index_empty_spaces:
        qc.x(qubit)

    qc.barrier()
    # Apply multiple controlled Z-gates
    qc.h(index_empty_spaces[-1])
    # Toffoli with multicontrol
    qc.mct(index_empty_spaces[:-1], index_empty_spaces[-1])
    qc.h(index_empty_spaces[-1])
    qc.barrier()
    # Apply transformation |11..1> -> |00..0>
    for qubit in index_empty_spaces:
        qc.x(qubit)
    # Apply transformation |00..0> -> |s>
    for qubit in index_empty_spaces:
        qc.h(qubit)

    # qc.measure([4,5,7,8],creg_c)

    return qc


def measurement(qc, board):
    """
    Adds the measurement operation to the quantum circuit.

    Args:
        qc (QuantumCircuit): Quantum circuit.
        board (list): The Tic Tac Toe board.

    Returns:
        QuantumCircuit: Quantum circuit with measurement operation.
    """
    one_dimensional_list = [value for row in board for value in row]
    index_empty_spaces = [i for i, value in enumerate(
        one_dimensional_list) if value == ' ']

    qc.measure(index_empty_spaces, qc.clbits)
    return qc



def grover_algorithm(board, rep=1):
    """
    Executes the Grover's algorithm for Tic Tac Toe.

    Args:
        board (list): The initial state of the Tic Tac Toe board.
        rep (int): Number of iterations of the algorithm.

    Returns:
        QuantumCircuit: Quantum circuit representing the Grover's algorithm.
    """
    qc = setting_initial_configuration(board)
    qc.barrier()

    for _ in range(rep):
        # Oracle
        qc = qc.compose(oracle())
        qc.barrier()
        # Diffuser
        qc = qc.compose(diffuser(board))
        qc.barrier()

    # Measurement
    qc = measurement(qc, board)
    qc.barrier()

    return qc


def circuit_execute(qc, shots=10000):
    """
    Executes the quantum circuit on a simulator.

    Args:
        qc (QuantumCircuit): Quantum circuit.
        shots (int): Number of shots for the simulation.

    Returns:
        dict: Counts of the measurement outcomes.
    """
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=shots)
    result = job.result()
    # Returns counts
    counts = result.get_counts(qc)

    counts_without_qiskit_convention = {
        key[::-1]: value for key, value in counts.items()}

    return counts_without_qiskit_convention

if __name__ == '__main__':
    # Example of usage
    from general_utils import generate_random_board

    num_moves = 5
    board = generate_random_board(num_moves)
    # print(board)
    qc_init = setting_initial_configuration(board)
    print(qc_init)

    # Oracle
    print(oracle())
    # print(diffuser(board))
