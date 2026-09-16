numeros = [2, 8, 5, 3, 9, 4, 1]
print(f"Lista original: {numeros}")
print(" ")

lista = list(numeros)
n = len(lista)
print("-- ORDENAMIENTO POR SELECCION --")

for i in range(n - 1):
    pos_min = i
    for j in range(i + 1, n):
        if lista[j] < lista[pos_min]:
            pos_min = j
    lista[i], lista[pos_min] = lista[pos_min], lista[i]
    print(f"Paso {i + 1}: {lista}")
print(" ")

lista = list(numeros)
n = len(lista)
print("-- ORDENAMIENTO POR BURBUJA --")

for i in range(n):
    for j in range(0, n - 1 - i):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            print(f"Paso {i + 1}: {lista}")
print(" ")

lista = list(numeros)
print("-- ORDENAMIENTO POR INSERCION --")

for i in range(1, len(lista)):
    clave = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > clave:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = clave
    print(f"Paso {i}: {lista}")
print(" ") 