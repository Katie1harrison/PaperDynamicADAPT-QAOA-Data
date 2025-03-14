from qiskit.circuit import QuantumCircuit
from qiskit.converters import circuit_to_dag

def extract_CNOT_network(append_clifford: QuantumCircuit):
    dag = circuit_to_dag(append_clifford.inverse())
    num_qubits = len(append_clifford.qubits)
    cnot_network = QuantumCircuit(num_qubits)
    hadamard_counts = [0] * num_qubits
    for node in dag.topological_op_nodes(): 
        if node.name == 's' or node.name == 'sdg':
            raise Exception("Circuit contains s or sdg gate")
        if node.name == 'h':
            hadamard_counts[node.qargs[0]._index] += 1

        if node.name == 'cx':
            control_qubit = node.qargs[0]._index 
            target_qubit = node.qargs[1]._index
            if max(hadamard_counts[node.qargs[0]._index], hadamard_counts[node.qargs[1]._index]) % 2 == 1:
                #Switch the control and the target qubit for even layers of hadamard gates
                temp = control_qubit 
                control_qubit = target_qubit
                target_qubit = temp
            cnot_network.cx(control_qubit, target_qubit)
    return cnot_network.inverse()

def apply_cnot(binary_value, control_index, target_index):
    # Convert binary string to a list of characters for easy manipulation
    binary_list = list(binary_value)
    # Apply CNOT: If the control qubit is 1, flip the target qubit
    if binary_list[control_index] == '1':
        binary_list[target_index] = '0' if binary_list[target_index] == '1' else '1'
    
    # Convert list back to binary string
    return ''.join(binary_list)

def update_probabilities(prob_dist, circuit_dag):
    updated_states = {}
    for state in prob_dist.keys():
        new_state = state
        for node in circuit_dag.topological_op_nodes():
            if node.name == 'cx':
                control_qubit = len(state) - node.qargs[0]._index - 1
                target_qubit = len(state) - node.qargs[1]._index - 1
                new_state = apply_cnot(new_state, control_qubit, target_qubit)
        updated_states[new_state] = prob_dist[state]
    return updated_states