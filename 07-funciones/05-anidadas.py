
def operacion( cantidad, valance, tipo='deposito' ):

    def deposito( cantidad, valance ):
        return cantidad + valance


    def retiro( cantidad, valance ):
        if( cantidad <= valance ):
            return valance - cantidad
        else:
            return None
    
    if tipo=='deposito':
        return deposito( cantidad, valance )
    if tipo=='retiro':
        return retiro( cantidad, valance )


resultado = operacion(10, 30, 'retiro')
print( resultado )
