#NOTES for JI
1. to run the code you have to choose the number of nodes for the graph, and the number of layers
2. src_code is where the Adapt QAOA functions are stored
3. something is not quite right with the ordering of the layers because when I go above 2layers, I get 66% fidelity instead of 99. We faced this problem previously, and I can't recall how we fixed it, I think it might be one of 2 things. either the order of layers should be swapped, or it has to do with the hadamard gates initialization at the beginning.

Please send me questions as they arise, and I will also try and fix them.
# Quantum Approximate Optimization Algorithms in Python

This is a package build in Python which lets users run versions of quantum algorithms used to solve the max-cut problem from graph theory, namely QAOAs. Three types of algorithms are supported:
- Standard QAOA
- ADAPT-QAOA
- Dynamic ADAPT-QAOA

## Usage
All the source code is available in the src_code directory of this repository.
The following imports are required:
- qiskit
- networkx
- scipy
- numpy
- pandas
- cvxpy

The IPython notebook package_demonstration.ipynb gives an example of how the algorithms may be run to solve a specific problem. An example Python script, run_multiple_graphs_parallelised.py, is also added, and shows how multiprocessing can be used to run the algorithm on multiple graphs simultaneously. It must be run 
from the terminal with the following arguments in this order:
- number of vertices of graphs
- number of graphs to solve for
- random generator seed for first graph (all other graphs are generated using consecutive seeds)
- maximum depth of circuit
- algorithm type, options include:
	- standard - Standard QAOA
    - adapt - ADAPT-QAOA
    - dynamic_adapt - Dynamic ADAPT-QAOA
    - dynamic_adapt_noisy - Dynamic ADAPT-QAOA with quantum circuits built in the presence of depolarising noise
    - dynamic_adapt_no_cost - ADAPT-QAOA with no cost unitaries in any layer
    - dynamic_adapt_zero_gamma - Dynamic ADAPT-QAOA where the originally found mixer is preserved in the case where the cost unitaries is kept in the current layer 
- output directory (must exist)
- gate-error probability (only in the case where a noisy simulator is chosen for the algorithm type)

Another script, run_circuits_with_noise.py, simulates previously built quantum circuits, but in the presence of noise. The following arguments are required:
- data_dir - directory containing data from the noiseless simulation of the quantum algorithm
- gate-error probability

## License
The code presented in this repository was written wholly by the distributor. The use of open source packages is acknowledged. # Quantum Approximate Optimisation Algorithms in Python
