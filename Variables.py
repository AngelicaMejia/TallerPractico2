a = 5
b = 'Angelica'
c = "Mejia"
d = 10,5
e = '10'

print("Mi nombres es {} y mi apellido es {}". format(b,c))
print(int(e))
dato = input('cual es tu nombre?: ')
print(dato)

num1 = 8
num2 = 5
num3 = 9

if num1 < num2:
    print('Num1 es menor de Num2')
elif num3 > num1:
    print('Num3 es mayor de Num1')
else:
    print('Num1 es mayor de Num2')
x = 1
while x <= 10:
    print(x)
    x = x + 1
z = 1
for z in range(1,10):
    print(z)
users = ['A','B','C']
for user in users:
    print(user)
def saludo():
    print('Hola Clases')
saludo()
def cuadrado(n):
    print(n*n)
cuadrado(8)
def MiNombre(n):
    return 'su nombre es {} y apellido Mejia'. format(n)
nom = MiNombre('Angie')
print(nom)

#tuplas
a = (1 , 2 , 3)
print(a)

#filas
var = ['bb','bb']
print(var)

#Diccionarios
vari = {'var1':'vari1','var2':'vari2'}
print(vari)
clase = [
    {'var1': 'vari1', 'var2': 'vari2'},
    {'var1':'vari1','var2':'vari2'},
    ('zjzjzj','jz')
]

#Tuplas en python
numeros = (1,2,3)
cadena = ('aaa','bbb','ccc')
varios = (1,'aaa',True,1.9)
for elemento in varios:
    print(elemento)
def enviar_datos():
    nombre = 'Jonathan'
    correo = 'jonmid@gmail.com'
    edad = 30
    ciudad = 'Pasto'
    return (nombre, correo, edad, ciudad)

def recibir_datos(datos):
    print(datos[0])
    print(datos[1])
    print(datos[2])

recibir_datos(enviar_datos())

# librerias en python
import random
# Obtener un numero aleatorio
numero = random.randint(1, 10)
print(numero)
# De la libreria "math" solo trae la funcion “sqrt"
from math import sqrt
n = sqrt(9) # Obtener la raiz cuadrada
print(n)

#MODULO TURTLE
#importa modulo
import turtle
#abre una ventana
winows = turtle.Screen()
#inicializa el dibujo
square = turtle.Turtle()
#dibuja
square.forward(25)
square.left(95)
square.forward(25)
square.left(95)
square.forward(25)
square.left(95)
square.forward(25)
square.left(95)
#mantener l dibujo en pantalla
turtle.mainloop()
