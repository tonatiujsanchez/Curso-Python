


""" 
 a -> funcion principal
 b -> funcion a decorar
 c -> funcion decorada

 a(b) -> c
"""

def funcion_a( funcion_b ):

    def funcion_c(*args, **kwargs):
        print('>>>Antes del llamado')

        result = funcion_b(*args, **kwargs)
        
        print('>>>Despues del llamado')

        return result
    
    return funcion_c


@funcion_a
def saludar():
    print('Hola nos encontramos en un función.')


@funcion_a
def suma(num1, num2):
    return num1 + num2


saludar()

resultado = suma(10, 20)
print(resultado)







