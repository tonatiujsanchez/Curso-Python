

# class <NombreClase>

# Attrs de clase
# Attrs de instancia

class Usuario:

    # Attrs de clase
    username = 'tonsanzjimz'
    email = ''


# ==== ==== ==== Atribitos de Clase ==== ==== ====

Usuario.username='brandon'
Usuario.email='brandon@gmail.com'

print(Usuario.username)
print(Usuario.email)



# ==== ==== ==== Atribitos de instancia ==== ==== ====
# __dict__
user_uno = Usuario()
# 1.- Verifica si el attr existe dentro del objeto
# 2.- Verifica si el attr existe dentro de la clase -> solo lectura
# 3.- Lanza un error su no lo encuentra
print( user_uno.username )


user_uno.username = 'tonsanz' # Añadimos el attr al objeto
user_uno.name = 'Tonatiuj' # Añadimos el attr al objeto
user_uno.password = '1234' # Añadimos el attr al objeto
print( user_uno.username )

print( user_uno.__dict__ )



