mi_lista = [4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 58, 65, 80, 98]

print("-- Programa de Busqueda de Vecinos --")
print(f"Lista disponible: {mi_lista}")

print("-" * 30)
try:
    entrada = input("Ingrese su número a buscar: ")
    numero_buscado = int(entrada)
except ValueError:
    print("Error!! Ingrese un número entero")
    exit()

posicion = -1

print(f"\nNúmero a buscar: {numero_buscado}")
for i, valor in enumerate(mi_lista):
    if valor == numero_buscado:
        posicion = i
        break

if posicion != -1:
    print(f"Número {numero_buscado} encontrado en la posicion {posicion + 1}")

    if posicion > 0:
        vecino_izquierda = mi_lista[posicion - 1]
        print(f"Vecino de izquierda (menor): {vecino_izquierda}")
    else:
        print("No hay un valor menor al escogido")

    if posicion < len(mi_lista) - 1:
        vecino_derecha = mi_lista[posicion + 1]
        print(f"Vecino de derecha (mayor): {vecino_derecha}")
    else:
        print("No hay un valor mayor al escogido")
else:
    print(f"El número {numero_buscado} no se encuenntra en la lista")
print("-" * 30)

print("Programa finalizando..")