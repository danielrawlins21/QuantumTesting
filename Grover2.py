# %%
from qiskit import Aer, QuantumCircuit, transpile, assemble
from qiskit.visualization import plot_histogram

# %%
def oracle_gate(n, k):
    oracle_circuit = QuantumCircuit(n+1, name="Oracle")
    
    # Configurar el oráculo
    for qubit in range(n):
        if (k >> qubit) & 1:
            oracle_circuit.x(qubit)
    
    # Implementar el oráculo con compuertas CX (CNOT)
    oracle_circuit.cx(range(n), n)
    
    # Deshacer los cambios en la entrada
    for qubit in range(n):
        if (k >> qubit) & 1:
            oracle_circuit.x(qubit)
    
    return oracle_circuit.to_gate()

# %%
def grover_circuit(n, oracle_gate, iterations):
    grover_circuit = QuantumCircuit(n+1, n)
    
    # Inicializar los qubits en superposición
    grover_circuit.h(range(n+1))
    
    # Implementar Grover's algorithm
    for _ in range(iterations):
        grover_circuit.append(oracle_gate, range(n+1))
        grover_circuit.h(range(n+1))
        grover_circuit.x(range(n+1))
        grover_circuit.h(n)
        
        # Implementar el oráculo con compuertas CX (CNOT)
        grover_circuit.append(oracle_gate, range(n+1))
        
        grover_circuit.h(n)
        grover_circuit.x(range(n+1))
        grover_circuit.h(range(n+1))
    
    # Medir los qubits
    grover_circuit.measure(range(n), range(n))
    
    return (grover_circuit,grover_circuit.draw(output="mpl"))

# %%
# Lista de ejemplo

#Lista original
lista = [25, 37, 47, 29, 8, 12, 44, 30, 24, 33, 15, 39, 46, 5, 22]

#Lista con el número en la primera posición
#lista = [8, 37, 47, 29, 25, 12, 44, 30, 24, 33, 15, 39, 46, 5, 22]

#Lista con el número en la última posición
#lista = [25, 37, 47, 29, 22, 12, 44, 30, 24, 33, 15, 39, 46, 5, 8]
# Valor a buscar
k = 8

# %%
# Encontrar la posición de k en la lista
posicion = lista.index(k)

# Número de bits necesario para representar la lista
n = len(bin(max(lista))) - 2

# %%
# Crear el oráculo y el circuito de Grover
oracle = oracle_gate(n, posicion)
grover_circuito,draw = grover_circuit(n, oracle, iterations=10)

# %%
draw

# %%
# Simular el circuito
simulador = Aer.get_backend('qasm_simulator')
resultados = simulador.run(transpile(grover_circuito, simulador)).result()
conteos = resultados.get_counts()

# %%
# Mostrar los resultados
print(conteos)
plot_histogram(conteos)

# %%
# Encontrar la posición más probable
posicion_mas_probable = int(max(conteos, key=conteos.get), 2)

# Imprimir resultados
print("Posición de {} en la lista:".format(k), posicion_mas_probable)

# %%
# Mostrar bits correspondientes a cada elemento en la lista
for estado, frecuencia in conteos.items():
    decimal = int(estado, 2)
    print(f"Bits para {decimal}: {estado}")


