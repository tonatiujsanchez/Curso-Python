#Docstring
#__doc__ (Modulos, Clases, Metodos y Funciones)

def suma( num_1, num_2 ):
    """ 
    La función suma 2 numero enteros

    Argumentos:
    num_1 (int) 
    num_2 (int) 

    Se retorna la suma de los parámetros.

    TODO:
        *
    
    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    300

    """
    return num_1 + num_2



# print(suma.__doc__)
# print( help(suma) )


# Ejecutar en la terminal para hacer el test mediante la documentación
# python -m doctest 11-documentar.py