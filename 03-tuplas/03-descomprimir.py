numeros = (1, 2, 3, 4, 5)
# uno, dos, tres, cuatro = 1, 2, 3, 4
# uno, dos, tres, cuatro, cinco = numeros[0], numeros[1], numeros[2], numeros[3], numeros[4]
uno, dos, tres, cuatro, cinco = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)


uno, dos, tres, *resto_numeros = numeros
print(resto_numeros)

# Ignora el resto de valores
uno, dos, tres, *_ = numeros


# Omitir un valor _
uno, _, tres, *_ = numeros
print(uno)
print(tres)


# Omitir valores
otros_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, *_, nueve, diez = otros_numeros

print(uno)
print(dos)
print(tres)
print(nueve)
print(diez)


