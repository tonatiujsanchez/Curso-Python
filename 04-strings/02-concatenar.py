

nombre = 'Brandon'
apellido = 'Hernandez'

# 
nombre_completo = nombre + ' ' + apellido
print( nombre_completo )

# 
nombre_completo_dos = 'Child: %s %s' %( nombre, apellido )
print(nombre_completo_dos)

# 
nombre_completo_tres = 'Boy: {} {}'.format( nombre, apellido )
print( nombre_completo_tres )

# 
nombre_completo_cuatro = 'Person: {nombre} {apellido}'.format(
    nombre = nombre, 
    apellido = apellido
)
print( nombre_completo_cuatro )


# 
nombre_completo_cinco = f'Hola! {nombre} {apellido}'
print(nombre_completo_cinco)