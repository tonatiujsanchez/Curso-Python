
lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
print(lista)

# Order lista - Ascendente
lista.sort()
lista.sort()
print(lista)

# Order lista - descendente
lista.sort(reverse=True)
print(lista)


# Numero mayor
lista.sort(reverse=True)
print('Mayor:', lista[0])
print( max(lista) )

# Numero menor
lista.sort()
print('Menor:', lista[0])
print( min(lista) )


# Saber si SI un elemento se encuente dentro de la lista
print( 10 in lista ) # False
print( 5 in lista )  # True

# Saber si NO un elemento se encuente dentro de la lista
print( 10 not in lista )  # True
print( 5 not in lista )  # False


