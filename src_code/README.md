# QAOA_CLEAR
Artifact for the QAOA_CLEAR paper
## Installation
Creating an anaconda virtual environment is recommended before installing.
```
conda create --name QAOA_CLEAR python=3.10
conda activate QAOA_CLEAR
```
Then clone the github repo:
```
git clone https://github.com/revilooliver/QAOA_CLEAR.git
cd QAOA_CLEAR
```

Install the required packages via pip:
```
pip install -r requirements.txt
```

## Testing
Run the VQE_observables.ipynb notebook to find the examples of optimizing the circuits and calculating the expectation values
Run the QAOA_probabilities.ipynb notebook to find the examples of absorbing the CNOT network in QAOA. The benchmark_QuCLEAR_qiskit.ipynb contains the code for running more comparisons
