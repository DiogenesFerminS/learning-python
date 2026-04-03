#functions

def saludar():
    print("¡Holaaa!")

saludar()

def saludar_a(nombre):
    print(f"¡Hola {nombre}!")

saludar_a("Diogenes")
saludar_a("Paolo")

def suma(a, b):
    return a + b

print(suma(2,3))

# Docsstring
def restar(a,b):
    """Resta dos numeros y devuelve el resultado"""

    return a - b

print(restar(10, 2))

def multiplicar(a, b = 2):
    return a * b

print(multiplicar(2))

# Argumentos por posicion

def describir_user(nombre, apellido, edad):
    print(f"{nombre} {apellido} {edad}")

describir_user("Diogenes", "Fermin", 20)

# Argumentos por nombre

describir_user(edad = 20, nombre="Paolo", apellido="Santella")

# Argumentos de longitud variable

def suma_de_numeros(*args):
    suma = 0
    for num in args:
        suma += num
    
    return suma

print(suma_de_numeros(1,2,3,4,5,6,7,8,9,10))

# Argumentos de longitud variable con nombre

def mostrar_informacion(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

mostrar_informacion(nombre="Diogenes", apellido="Fermin", edad=20)

mostrar_informacion(nombre="Paolo", apellido="Santella", edad=20, ciudad="Campobasso")