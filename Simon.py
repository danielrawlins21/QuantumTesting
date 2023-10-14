from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram

# Longitud de la cadena binaria (n)
n = 3

# Crear un circuito cuántico con dos registros de n qubits cada uno
simon_circuit = QuantumCircuit(2 * n, n)

# Aplicar una puerta Hadamard a los primeros n qubits
for qubit in range(n):
    simon_circuit.h(qubit)

# Oráculo: Representación de una función dos a uno (en este ejemplo, s = '110')
s = '110'
for qubit in range(n):
    if s[qubit] == '1':
        simon_circuit.cx(qubit, n + qubit)  # Aplicar una puerta CNOT entre los registros

# Aplicar una puerta Hadamard a los primeros n qubits
for qubit in range(n):
    simon_circuit.h(qubit)

# Medir los primeros n qubits
simon_circuit.measure(range(n), range(n))

# Ejecutar el circuito en un simulador
simulator = Aer.get_backend('qasm_simulator')
job = execute(simon_circuit, simulator, shots=1024)
result = job.result()
counts = result.get_counts()

# Mostrar el resultado
plot_histogram(counts)
