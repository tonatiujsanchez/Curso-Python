
class Usuario:

    def inicializar( self, username, password ):
        # Añadiendo atrrs al objeto
        self.username = username
        self.password = password



user_uno = Usuario()
user_dos = Usuario()

user_uno.inicializar( 'tonsanzjimz', '123456' )
user_dos.inicializar( 'brantiago', '987456')

print( user_uno.__dict__ )
print( user_dos.__dict__ )