
# Las tuplas no son mutables
#       num     str    bool  float      list       tuple
tupla = (10, 'String', True, 3.14, ['a', 'b', 'c'],(1,2,3))

print(tupla)
print(type(tupla))

# Obtener un elemento mendiante el indice
print( tupla[4] )


# Subtupla:(Funciona como las listas)
sub_tupla = tupla[0:3]
print(sub_tupla)