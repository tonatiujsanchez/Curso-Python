

mensaje = 'Hola mundo'
print(mensaje)

# ljust  -> Alinear a la hisquierda
# rjust  -> Alinear a la derecha
# center -> Alinear al centro


izquierda = mensaje.ljust(20)
print(izquierda, '.')


derecha = mensaje.rjust(20)
print(derecha)

centrado = mensaje.center(20)
print(centrado)