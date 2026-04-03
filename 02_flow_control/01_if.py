from enum import nonmember
import os

os.system("clear")

edad = int(input("Ingresa tu edad:\n"))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


note = int(input("Ingresa tu nota:\n"))

if note >= 19:
    print("Excelente")
elif note >= 17:
    print("Muy bueno")
elif note >= 14:
    print("Bueno")
elif note >= 11:
    print("Regular")
else:
    print("Deficiente")

print("Alumno Evaluado!!")

has_license = False

if edad >= 18 and has_license:
    print("Puedes conducir")
else:
    print("No puedes conducir")

if edad >= 18 or has_license:
    print("Puedes conducir")
else:
    print("POLICIAAAAAA!")

is_weekend = False

if not is_weekend: 
    print("Es dia de semana a trabajar")
else: 
    print("A descansar")

print("Condiciones anidadas \n")

has_money = True

if edad >= 18:
    if has_money:
        print("Puedes comprar alcohol")
    else:
        print("Ponte a trabajar")
else:
    print("No puedes comprar alcohol")

os.system("clear")
numero = 4

if numero:
    print("Hay un numero")
else: 
    print("No hay un numero")

nombre = " "

if nombre:
    print("Hay un nombre")
else: 
    print("No hay un nombre")

os.system("clear")

ternario = False

print("Operadores ternarios true" if ternario else "Ternario es False")