namespace Ejemplo {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    operation HolaMundo() : Unit {
        // Aloca un qubit.
        use q = Qubit();

        // Aplica la operación de Hadamard al qubit.
        H(q);

        // Mide el qubit.
        let resultado = M(q);

        // Imprime el resultado de la medición.
        Message($"El resultado es {resultado}");
        
        // Asegura que el qubit esté en el estado |0⟩ antes de liberarlo.
        Reset(q);
    }
}
