import os 
os.system("clear")

print("\nList methods")

list1 = ["a", "b", "c", "d"]

# add elements on list
list1.append("e")
print(list1)

list1.insert(1, "@")
print(list1)

list1.extend(["diogenes", "good", "@"])
print(list1)

# remove elements on list
list1.remove("@")
print(list1)

ultimo = list1.pop()
print(f"Elemento eliminado: {ultimo}")
print(list1)

del list1[-1]
print(list1)
# list1.clear() para borrar todo

# Metodos utiles
print("Ordenar listas modificando la original")
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print("Ordernar listas con una copia")
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minusculas)")

fruits = ["manzana", "pera", "limon", "manzana", "pera", "limon"]
sorted_fruits = sorted(fruits)
print(sorted_fruits)

print("Ordenar una lista de cadenas de texto (mezclas mayuscular y minusculas)")

fruits = ["manzana", "Pera", "Limon", "manzana", "pera", "limon"]
fruits.sort(key=str.lower)
print(fruits)

# Others methods
animals = ["gato", "perro", "aguila", "leon"]
print(len(animals))
print(animals.count("gato")) # cuantas veces esta "gato" en la lista
print("leon" in animals)