numeroUno = int(input('Digite  primer valor numerico: '))
numeroDos = int(input('Digite segundo valor numerico: '))
print('LAS OPERACIONES A REALIZAR SON: ')
print('SUMA - RESTA - MULTIPLICACION - DIVISION')
operacion = input('Digite operacion a realizar numerico: ')
if operacion == 'SUMA' :
    resultado = numeroUno + numeroDos
elif operacion == 'RESTA' :
    resultado = numeroUno - numeroDos
elif operacion == 'MULTIPLICACION' :
    resultado = numeroUno * numeroDos
elif operacion == 'DIVISION':
    resultado = numeroUno / numeroDos

print (resultado)