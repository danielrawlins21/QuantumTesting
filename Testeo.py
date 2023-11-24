def calcular_deflexion(W, L, E, a):
    # Calcular el momento flector máximo
    M = W * L / 2
    
    # Calcular el segundo momento de área
    I = a**4 / 12
    
    # Calcular la deflexión máxima
    delta = (W * L**3) / (48 * E * I)
    
    return delta

# Datos para cada material
W = 1500 * 9.8  # Peso en Newtons
L = 5  # Longitud de la viga en metros
a = 0.15  # Lado de la sección transversal en metros

# Datos para cada material: módulo de elasticidad (en Pascal)
E_aluminio = 70e9
E_madera = 12e9
E_hierro = 200e9

# Calcular deflexiones para cada material
delta_aluminio = calcular_deflexion(W, L, E_aluminio, a)
delta_madera = calcular_deflexion(W, L, E_madera, a)
delta_hierro = calcular_deflexion(W, L, E_hierro, a)

# Imprimir resultados
print("Deflexión máxima para Aluminio:", delta_aluminio, "metros")
print("Deflexión máxima para Madera de pino:", delta_madera, "metros")
print("Deflexión máxima para Hierro:", delta_hierro, "metros")
