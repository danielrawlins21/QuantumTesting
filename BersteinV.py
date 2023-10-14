from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram

# Longitud de la cadena secreta (n)
n = 4

# Crear un circuito cuántico con n+1 qubits (el último qubit se utiliza para medir)
bv_circuit = QuantumCircuit(n+1, n)

# Aplicar una puerta Hadamard a todos los qubits, excepto el último
for qubit in range(n):
    bv_circuit.h(qubit)

# Oráculo: Representación de la cadena secreta 's' (en este ejemplo, s = '1010')
s = '1010'
for qubit in range(n):
    if s[qubit] == '1':
        bv_circuit.cx(qubit, n)  # Aplicar una puerta CNOT al último qubit controlado por qubit

# Aplicar una puerta Hadamard a todos los qubits, excepto el último
for qubit in range(n):
    bv_circuit.h(qubit)

# Medir los primeros n qubits
bv_circuit.measure(range(n), range(n))

# Ejecutar el circuito en un simulador
simulator = Aer.get_backend('qasm_simulator')
job = execute(bv_circuit, simulator, shots=1024)
result = job.result()
counts = result.get_counts()

# Mostrar el resultado
plot_histogram(counts)
