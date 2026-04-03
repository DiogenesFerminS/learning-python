import os
# While

#contador = 0

# while contador <= 5:
   # print(contador)
   # contador += 1


# While con break

os.system("clear")

print("\n<=== While con break ===>")

contador = 0
while True:
    print(contador)
    contador += 1
    
    if contador % 5 == 0:
        print("El contador es multiplo de 5")
        break

# While con continue

# os.system("clear")

print("\n<=== While con continue ===>")

contador = 0
while contador <= 10:
    contador += 1

    if contador % 2 == 0:
        continue

    print(contador)

#While con else

print("\n<=== While con else ===>")
contador = 0

while contador <= 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")


#While con else y break

print("\n<=== While con else y break ===>")

contador = 0
while contador <= 5:
    print(contador)
    contador += 1
    break
else:
    print("Bucle terminado")

# Ejercicio 

print("\n <=== Ejercicio ===> \n")
numero = -1

while numero < 0:
    try:
        numero = int(input("Introduce un numero positivo: \n"))
        if numero < 0:
            print("El numero debe ser positivo")
    except:
        print("Error: debes introducir un NUMERO")

print(f"El numero introducido por el usuario es: {numero}")
        