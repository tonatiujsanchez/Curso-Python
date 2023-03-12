
# ==== ==== ==== ESCOPE ==== ==== ==== 
print('==== ==== ==== ESCOPE ==== ==== ====')

e='e' # global

def funcion_principal():
    a = 'a' # local
    b = 'b' # local

    def funcion_anidada():
        c = 'c' # local

        nonlocal b #Para referirno a una variable en un nivel superior
        b = 'Otro valor'

        print(a)
        print(b)

        print(e)
    
    funcion_anidada()
    print(b)

funcion_principal()


# ==== ==== ==== FUNCIONES ==== ==== ==== 
print('==== ==== ==== FUNCIONES ==== ==== ====')

def saludar ():
    def mostrar_mensaje():
        print('Hola estamos en el curso de Python')
    return mostrar_mensaje

resp = saludar()
print(resp() )


# ==== ==== ==== CLOUSURE ==== ==== ==== 
print('==== ==== ==== CLOUSURE ==== ==== ====')
def saludar( username ):
    mensaje = f'Hola { username }.'

    def mostrar_mensaje():
        print(mensaje)
    
    return mostrar_mensaje

username = 'Brandon'
respuesta = saludar(username)

respuesta()
