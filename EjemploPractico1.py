import turtle


dato = int(input('Digite valor numerico: '))



#abre una ventana
windows = turtle.Screen()

#inicializa el dibujo
square = turtle.Turtle()

#dibuja
def dibujo(dato) :
    for i in range(1,5):
        square.forward(dato)
        square.left(90)

#mantener l dibujo en pantalla
dibujo(dato)


turtle.mainloop()