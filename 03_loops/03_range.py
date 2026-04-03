# range()
# crea un secuencia de numeros
# range(stop)
# range(start, stop)
# range(start, stop, step)

print("\n <=== Range ===> \n")

nums = range(5)
print(nums)

print("\n <=== Range con stop ===> \n")
for num in range(10):
    print(num)

print("\n <=== Range con start y stop ===> \n")
for num in range(5, 10):
    print(num)

print("\n <=== Range con start, stop y step ===> \n")
for num in range(0, 10, 2):
    print(num)

for _ in range(5):
    print("Hacer cinco veces algo")


