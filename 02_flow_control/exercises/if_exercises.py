import os 

os.system("clear")

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("<==== Ejercicio 1 ====>")
num1 = int(input("Introduce el primer numero: \n"))
num2 = int(input("Introduce el segundo numero: \n"))

if num1 > num2: 
    print(f"{num1} es mayor que {num2}")
elif num2 > num1: 
    print(f"{num2} es mayor que {num1}")
else:
    print("Los numero son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
os.system("clear")

print("<==== Ejercicio 2 ====>")
numero1 = int(input("Introduce el primer numero: \n"))
numero2 = int(input("Introduce el segundo numero numero: \n"))

operacion = int(input(""" 
    <==== Calculadora ====>
1. Suma
2. Resta
3. Multiplicacion
4. Division
"""))

match operacion:
    case 1:
        print(f"El resultado de la operacion es: {numero1 + numero2}")
    case 2:
        print(f"El resultado de la operacion es: {numero1 - numero2}")
    case 3: 
        print(f"El resultado de la operacion es: {numero1 * numero2}")
    case 4:
        print(f"El resultado de la operacion es: {numero1 / numero2}")
    case _:
        print(f"Operacion no soportada")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

os.system("clear")

print("<==== Ejercicio 3 ====>")

year = int(input("Introduce un año: \n"))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Es año bisiesto")
else: 
    print("No es año bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("<==== Ejercicio 4 ====>")

edad = int(input("Introduce tu edad: \n"))

if edad <= 2:
    print("Eres un bebe")
elif edad <= 12:
    print("Eres un niño")
elif edad <= 17:
    print("Eres un adolescente")
elif edad <= 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
