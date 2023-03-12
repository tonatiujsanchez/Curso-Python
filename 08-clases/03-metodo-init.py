
class Usuario:

    def __init__( self, username='', password='' ):
        self.username = username
        self.password = password


user_uno  = Usuario('user1', '112356')
user_dos  = Usuario('user2', '265756')
user_tres = Usuario('user3', '395456')
user_cuatro = Usuario()

print( user_uno.__dict__ )
print( user_dos.__dict__ )
print( user_tres.__dict__ )
print( user_cuatro.__dict__ )