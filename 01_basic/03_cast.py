print("Conversion de tipos")

#INT CAST

print(type("100"))
print(type(int("100")))

print(2 + int("100"))

#FLOAT CAST
print(type(float("3.1416")))
print(int(3.1416))

#BOOL CAST
print(bool(3))
print(bool(0))
print(bool(-1))

print(bool(""))
print(bool(" "))
print(bool("False"))


#ROUND
# SI EL NUMERO ESTA JUSTO A LA MITAD REDONDEA AL PAR MAS CERCANO
print(round(2.5))
print(round(2.6))
print(round(3.5))
