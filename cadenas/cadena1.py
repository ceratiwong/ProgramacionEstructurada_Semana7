#Cadena de caracteres
nombre = "Michael Alejandro Wong Espinoza"
print(nombre)

texto = "    "
cadena = " Jesucristo "

print("Nombre: ", end = " ")
print(nombre)
print("Texto: ", end = " ")
print(texto)

#Tamaño de la cadena
print("Nombre: ", end = " ")
print(len(nombre))
print("Texto: ", end = " ")
print(len(texto))

texto += nombre

print("Nombre: ", end = " ")
print(len(nombre))
print("Texto: ", end = " ")
print(len(texto))

print("Nombre: ", end = " ")
print(nombre)
print("Texto: ", end = " ")
print(texto.strip())

