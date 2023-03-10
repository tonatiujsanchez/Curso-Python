
diccionario = { 'a': 1, 'b':2, 'c':3, 'd':4 }


valor_a = diccionario['a']  # si no exite da un error
valor_b = diccionario['b']
print(valor_a)
print(valor_b)


# get()
valor_d = diccionario.get('d')
print( valor_d )
valor_z = diccionario.get('z') #So no existe devuelde 'None'
print( valor_z )


# Podemos asiganr un valor por defecto de cualquier tipo(Str, Bool, Int, Float, etc) en cado de que no exista
valor_x = diccionario.get('x', 'La llave no exite')
print( valor_x )


# Obtiene el valor y en caso de no exita la crea con el valor inidcado
valor_e = diccionario.setdefault('e', 5)
print(valor_e)
print(diccionario)