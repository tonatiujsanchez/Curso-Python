
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su nombre: ')
anio_nacimento = input('Ingrese su año de nacimiento: ')
altura_input = input('Ingrese su altura: ')

edad = 2023 - int( anio_nacimento ) 
altura = float( altura_input )

print( 'Su nombre completo es:', nombre, apellido,', tiene', edad, 'años y mide', altura, 'm'  )


confirmacion_usuario = input('¿Tus datos con correctos? (si/no): ')

confirmacion = confirmacion_usuario == 'si'

print(confirmacion)