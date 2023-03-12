
promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7


def mostrar_mensaje( func_promedio, func_aprobatorio, *args ):

    promed = func_promedio(*args)
    mensaje = f'Felicidades has aprobado con { promed }' if func_aprobatorio( promed ) else f'No Aprobado, tienes {promed}'

    print( mensaje )

    
mostrar_mensaje( promedio, aprobatorio, 9,10,9,10, 5, 4, 1  )