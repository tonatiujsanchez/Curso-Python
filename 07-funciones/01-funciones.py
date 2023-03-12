def suma(n1, n2):
    return n1 + n2, 'Se sumó correctamente'


numero_uno = int(input('Ingrese el primer numero entero: '))
numero_dos = int(input('Ingrese el segundo numero entero: '))


resultado, mensaje = suma( numero_uno, numero_dos )
print(mensaje)
print( 'El resultado es:', resultado )
