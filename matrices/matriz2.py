matriz = []

filas = 0
columnas = 0

def pedir_tamaño(i, j):
    global filas, columnas
    filas = int(input("Tamaño de filas: "))
    columnas = int(input("Tamaño de columnas: "))

def leer_valor(mensaje):
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
            matriz[i].append(int(input(f"Valor ({i+1}, {j+1}): ")))
            matriz[i].append(dato)

def menu():
    print("""
1. Asignar tamaño
2. Asignar elemento
3. Salir
""")
    op = leer_valor("Opción: ")
    return op

def main():
    while True:
        op = menu()
        if op == 1:
            pedir_tamaño()
        elif op == 2:
            agregar_elemento()
        elif op == 3:
            print("Adiós")
            break