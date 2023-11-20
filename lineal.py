def buscar(lista, k):
    for i in range(len(lista)):
        if lista[i] == k:
            return i
    return -1

lista = [25, 37, 47, 29, 8, 12, 44, 30, 24, 33, 15, 39, 46, 5, 22]
k = 8
print(buscar(lista, k))  # Debería imprimir 4
