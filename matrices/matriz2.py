matriz = []

filas = 0
columnas = 0

def pedir_tamaño(i, j):
    global filas, columnas
    filas = i
    columnas = j

def leer_valor():
    while True:
        try:
            valor = int(input("Dime un valor numérico: "))
            return valor
        except ValueError:
            print("Error. Verifique que el valor sea entero.")

def agregar_elemento():
    for i in range(filas):
        matriz.append([])
        for j in range (columnas):
            matriz[i].append(int(input(f"Valor ({i}, {j}): ")))

pedir_tamaño(2, 2)
print(filas, columnas)
agregar_elemento()