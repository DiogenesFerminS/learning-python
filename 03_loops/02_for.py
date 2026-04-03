import os
# For

print("\n <=== For ===> \n")

# Iterar lista
frutas = ["manzana", "pera", "limon", "uva"]

for fruta in frutas:
    print(fruta)

# Iterar cadena
cadena = "diogenes"
for caracter in cadena:
    print(caracter)

# enumerate()
for index, fruta in enumerate(frutas):
    print(f"Indice: {index}, Fruta: {fruta}")

# bucles anidados
letras = ["A", "B", "C"]
numeros = [1,2,3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

# for con break

animales = ["perro", "gato", "raton", "loro", "pez", "canario"]

for index, animal in enumerate(animales):
    print(animal)
    if animal == "raton":
        print(f"El raton esta en la posicion {index}")
        break

# Comprension de listas 

print("\n <=== Comprension de listas ===> \n")

os.system("clear")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Compresion con condicional

print("\n <=== Comprension con condicional ===> \n")

numbers = [1, 2, 3, 4, 5, 6]

pares = [num for num in numbers if num % 2 == 0]
print(pares)