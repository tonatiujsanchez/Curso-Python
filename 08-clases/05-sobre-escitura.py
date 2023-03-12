class Animal: # Clase padre

    def comer(self):
        print('Animal Comiendo...')

    def dormir(self):
        print('Animal Durmiendo...')


class Mascota(Animal): # Clase padre
    
    def jugar(self):
        print('Mascota Jugando...')

    def comer(self):
        print('Mascota Comiendo...')


class Felino:

    def cazar(self):
        print('Falino Cazando...')


class Gato( Mascota, Felino ):
    
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f'El Gato {self.nombre} esta Comiendo...')


polin = Gato('Polín')
polin.comer()
polin.dormir()

print(polin.__dict__)