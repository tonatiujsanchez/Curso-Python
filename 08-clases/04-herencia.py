
class Animal: # Clase padre

    def comer(self):
        print('Animal Comiendo...')

    def domir(self):
        print('Animal Durmiendo...')


class Mascota(Animal): # Clase padre
    
    def jugar(self):
        print('Mascota Jugando...')
    

class Felino:

    def cazar(self):
        print('Falino Cazando...')


# Herencia
class Perro( Mascota ): #Clase hija
    pass

hook = Perro()
# hook.comer()
# hook.domir()



# Herencia múltimple
class Gato( Mascota, Felino ):
    pass


redux = Gato()
redux.comer()
redux.jugar()
redux.cazar()