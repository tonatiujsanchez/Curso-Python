
#                  0            1         2       3       4
lista_cursos = ['Python', 'Javascript', 'PHP', 'Dart', 'Java']
#                  -5          -4        -3     -2      -1

primer_elemento = lista_cursos[0]
print( primer_elemento )

segundo_curso = lista_cursos[1]
print(segundo_curso)


ultimo_curso = lista_cursos[-1]
print(ultimo_curso)


# ==== ==== Actualizaru Elemento ==== ====

print( lista_cursos )
lista_cursos[4] = 'GO'
print( lista_cursos )


# ==== ==== Sublistas ==== ====
                        #[inicio:final] 
sub_lista = lista_cursos[1:3]
print( sub_lista )

                    #[inicio:]   #Indicamos el indice inicial y agrega el resto
sub_lista = lista_cursos[1:]
print( sub_lista )


                    #[:final]   #Solo inidicamo el final y agrega todos los anteriores
sub_lista = lista_cursos[:4]
print( sub_lista )


                    # [inico:final/skip] #Saltar elementos de 2 en 2
sub_lista = lista_cursos[1:4:2] 
print( sub_lista )

# Copiamos todos los elementos
sub_lista = lista_cursos[:] 
print( sub_lista )

# Copiamos todos los elementos invirtiendo el orden
sub_lista = lista_cursos[::-1] 
print( sub_lista )


