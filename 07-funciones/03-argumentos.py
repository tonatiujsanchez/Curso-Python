
# se almacenan en una tupla
def promedio( *args ):
    return sum(args) / len(args)


resultado = promedio(10, 10, 7, 8, 9, 10)
print(resultado)

# se almacenan en una tupla
def convinacion( p1, *args, p6=100 ):
    print(p1, args, p6)

convinacion(1, 2, 3, 4, 5, p6=500)


# se almacenan en un diccionario
def usuarios(**kwargs):
    print(kwargs)


usuarios(eduardo=[10, 10, 9], fernando=[9,9,10])



# se almacenan en un diccionario y una tupla
def conbinacion(*args, **kwargs):
    print(args)
    print(kwargs)


conbinacion(1,2,3,4,5,6,7, user=True, curos='Python')