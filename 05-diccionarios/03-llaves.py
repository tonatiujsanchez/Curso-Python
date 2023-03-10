
diccionario = { 'a':1, 'b':2, 'c':3, 'd':4 }


#keys
#values
#items

# Obtener las llaves del diccionario
llaves = diccionario.keys()
# Convertirlo en un tupla
llaves = tuple(diccionario.keys())
print('llaves:', llaves)


# Obtener solo los valores
valores = diccionario.values()
# Convertir en un tupla
valores = tuple( diccionario )
print('valores:', valores)


# Obtener elementos
elementos = diccionario.items()
# Convertir en tupla
elementos = tuple(diccionario.items())
print('elementos:', elementos)