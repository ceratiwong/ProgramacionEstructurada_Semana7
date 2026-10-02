def nombre_completo(nombres, apellidos):
    return f"{nombres} {apellidos}"

def nombre_completo_mayuscula(nombres, apellidos):
    return f"{nombres} {apellidos}".upper()

def nombre_completo_minuscula(nombres, apellidos):
    return f"{nombres} {apellidos}".lower()

def nombre_completo_capitalizable(nombres, apellidos):
    return f"{nombres.capitalize()} {apellidos.capitalize()}"

def nombre_completo_titulo(nombres, apellidos):
    return f"{nombres} {apellidos}".title()

def generar_correo(nombres, apellidos):
    return f"{nombres[:3].lower()}.{apellidos[:3].lower()}@uamv.edu.ni"

nombres = input("Dime tus nombres: ")
apellidos = input("Dime tus apellidos: ")

print("Nombre completo como tal ingresado: " + nombre_completo(nombres, apellidos))
print("Nombre completo en mayúsculas: " + nombre_completo_mayuscula(nombres, apellidos))
print("Nombre completo en minúsculas: " + nombre_completo_minuscula(nombres, apellidos))
print("Nombre completo capitalizable: " + nombre_completo_capitalizable(nombres, apellidos))
print("Nombre completo título: " + nombre_completo_titulo(nombres, apellidos))
print("Correo: " + generar_correo(nombres, apellidos))