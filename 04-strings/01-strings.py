
# Separar un String en una Lista
lenguages = 'Python-Ruby-Java-PHP-Dart'

lista = lenguages.split('-')
print(lista)

lista = lenguages.split('-', 2) #Número de veces a dividir
print(lista)



# Unir una lista en un String
lista_lenguages = ['Dart', 'Python', 'PHP', 'Javascript']

lenguages_string = ' '.join(lista_lenguages)
print( lenguages_string )