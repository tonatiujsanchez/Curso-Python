

titulo_curso = 'Curso profesional de Python'

# Devuelve la cantidad de veces que exite un string dentro de otro string
contador = titulo_curso.count('o')      #Int
contador = titulo_curso.count('python') #Int

print( contador )


# Saber si existe un string dentro de otro
# ( Es case sensitive )
print( 'python' in titulo_curso )  #Bool


# Bucar convirtiendo en Minusculas
print( 'python'.lower() in titulo_curso.lower() )  #Bool

# Bucar convirtiendo en Mayusculas
print( 'python'.upper() in titulo_curso.upper() )  #Bool

# Negar
print( 'python'.lower() not in titulo_curso.lower() )  #Bool


# Conocer si un string Empieza con la palabra curso
print( titulo_curso.startswith('curso') ) #False
print( titulo_curso.lower().startswith('curso'.lower()) ) #True


# Conocer si un string Termina con la palabra python
print( titulo_curso.endswith('curso') ) #False
