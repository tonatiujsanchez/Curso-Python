
#                  0            1         2       3       4
lista_cursos = ['Python', 'Javascript', 'PHP', 'Dart', 'Java']
#                  -5          -4        -3     -2      -1

# Obtener length -> len()
print( len(lista_cursos) )


# Insertar un elemento al final
lista_cursos.append('GO')
print(lista_cursos)
print( len(lista_cursos) ) #length

lista_cursos.append('Mongo')
print(lista_cursos)
print( len(lista_cursos) ) #length


# Insertar un elemento en una posision en especifico
lista_cursos.insert(2, 'C#')
print( lista_cursos )
# Insertar un elemento al inicio


# Concatenar otra lista al final
lista_frameworks = ['Angular', 'React', 'Ionic', 'React Native', 'NextJS','NodeJS']
lista_cursos.extend(lista_frameworks)
print(lista_cursos)


# ==== Eliminar elementos ==== 
# Por nombre
print(lista_cursos)
lista_cursos.remove('Mongo')
print(lista_cursos)

# Por inidice
del lista_cursos[0]
print(lista_cursos)


# Eliminar todos los elementos
lista_cursos.clear()
print(lista_cursos)
