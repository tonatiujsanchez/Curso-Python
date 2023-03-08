


lista = [ 1, 2, 3, 4, 5 ]

tupla = ( 10, 20, 30, 40, 50 )

lista_dos = [ 100, 200, 300, 400, 500 ]

tupla_dos = ( 1000, 2000, 3000, 4000 )


resultado = zip(lista, tupla, lista_dos, tupla_dos ) # -> zip
resultado = tuple(resultado) # -> tupla


print(resultado)