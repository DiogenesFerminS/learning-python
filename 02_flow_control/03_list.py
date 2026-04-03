import os
print("\nCrear Listas")

numbers = [1,2,3,4,5,6]
fruits = ["Manzana", "Pera", "Uva", "Naranja", "Sandia"]
mix_list = [1, "Hola", 3.14, True, [1,2,3]]

empty_list = []
list_of_list = [[1,2,3], [4,5,6], [7,8,9]]
matrix = [[1,2], [2,3], [4,5]]

print(numbers)
print(fruits)
print(mix_list)
print(empty_list)
print(list_of_list)
print(matrix)

print("\nList access")

print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(matrix[0][0])

os.system("clear")

print("\nSlicing")

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])

# Add elements on list
list1 = [1,2,3]

# Slow way
list1 = list1 + [4,5,6]
print(list1)

# Fast way
list1 += [7,8,9]
print(list1)

# list length
print("\nList length: ", len(list1))