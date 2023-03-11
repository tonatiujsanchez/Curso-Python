


titulo_curso = 'Curso profesional de Python'

# Termina cuando se cumple la condicion
for caracter in titulo_curso:
    if caracter == 'p':
        break
    print(caracter)

# Salta la iteración cuando la condición se cumple
for caracter in titulo_curso:
    if caracter == ' ':
        continue
    print(caracter)