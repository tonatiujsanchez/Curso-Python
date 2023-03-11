
calificacion = 10
color = None

# Version tradicional
if calificacion >= 7 :
    color = 'verde'
else:
    color = 'rojo'
print( calificacion, color )


# Ternario
color = 'verde' if calificacion >= 7 else 'rojo'
print( calificacion, color )
