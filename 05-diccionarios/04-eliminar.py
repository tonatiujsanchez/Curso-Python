
diccionario = { 'a':1, 'b':2, 'c':3, 'd':4 }
print(diccionario)


# 1 - Eliminar un elemento (Si no exite da un error)
del diccionario['a']
print(diccionario)


# 2 - Eliminar un elemento y obtener el valor del elemento eliminado (Si no exite da un error)
valor = diccionario.pop('b')
print(diccionario)
print(valor)


# 3 - Eliminar todos los elementos
diccionario.clear()
print(diccionario)
