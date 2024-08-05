#Importamos los modulos necesarios.
import turtle

#Creacion de una ventana
wn = turtle.Screen() #wn -> window
wn.title("Juego Pong") #Colocando titulo
wn.bgcolor("black") #Color de ventana
wn.setup(width = 800, height = 600) #Redireccionar la ventana
wn.tracer(0) #Animacion fluida

#Marcador para ir incrementando al hacer un punto
marcador1 = 0
marcador2 = 0

#Jugador1 -> creacion de objetos
jugador1 = turtle.Turtle()
jugador1.speed(0) #velocidad para que aparezca el objeto de manera instantanea cuando abro la ventana 
jugador1.shape("square") #La forma que va a tener el objeto, en este caso un cuadrado
jugador1.color("white") #Color de fondo
jugador1.penup() #Este comando evita una linea que sale al crear un objeto
jugador1.goto(-350,0) #Coordenadas para que aparezca
jugador1.shapesize(stretch_wid=5, stretch_len=1) #Aca estamos alargando la forma del cuadrado

#Jugador2 -> creacion de objetos
jugador2 = turtle.Turtle()
jugador2.speed(0) #velocidad para que aparezca el objeto de manera instantanea cuando abro la ventana 
jugador2.shape("square") #La forma que va a tener el objeto, en este caso un cuadrado
jugador2.color("white") #Color de fondo
jugador2.penup() #Este comando evita una linea que sale al crear un objeto
jugador2.goto(350,0) #Coordenadas para que aparezca
jugador2.shapesize(stretch_wid=5, stretch_len=1) #Aca estamos alargando la forma del cuadrado

#Pelota -> creacion de objetos
pelota = turtle.Turtle()
pelota.speed(0) #Velocidad para que aparezca el objeto de manera instantanea cuando abro la ventana 
pelota.shape("circle") #La forma que va a tener el objeto, en este caso un cuadrado
pelota.color("white") #Color de fondo
pelota.penup() #Este comando evita una linea que sale al crear un objeto
pelota.goto(0,0) #Coordenadas para que aparezca
pelota.dx = 0.3 #Esto es para que la pelota se mueva cada tantos pixeles en x
pelota.dy = 0.3 #Esto es para que la pelota se mueva cada tantos pixeles en y

#Linea divisoria
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#Puntuacion
pen = turtle.Turtle()
pen.speed(0) #Velocidad para que aparezca el objeto de manera instantanea cuando abro la ventana 
pen.color("white") #Color del marcador
pen.penup() #Este comando evita una linea que sale al crear un objeto
pen.hideturtle() #Por defecto al usar turtle se crea una imagen, con este comando la borramos
pen.goto(0,260) #Posicion arriba del todo
pen.write("Jugador1: 0      Jugador2: 0", align="center", font=("courier", 15, "normal")) #El marcador empieza en 0, centrado, fuente

#Funciones para crear el movimiento de los objetos y conectarlas con el teclado
def jugador1_up():
    y = jugador1.ycor() 
    y += 20 #Aumento la variable y por 20 pixeles para que se vaya hacia arriba
    jugador1.sety(y)

def jugador1_down():
    y = jugador1.ycor() 
    y -= 20 #Disminuyo la variable y por 20 pixeles para que se vaya hacia abajo
    jugador1.sety(y)

def jugador2_up():
    y = jugador2.ycor() 
    y += 20 #Aumento la variable y por 20 pixeles para que se vaya hacia arriba
    jugador2.sety(y)

def jugador2_down():
    y = jugador2.ycor() 
    y -= 20 #Disminuyo la variable y por 20 pixeles para que se vaya hacia abajo
    jugador2.sety(y)

#Conexion de funciones con el Teclado
wn.listen() #La ventana escucha si sucede un evento
wn.onkeypress(jugador1_up, "w") #Cuando se presiona una tecla(w), usamos la funcion que le pasamos
wn.onkeypress(jugador1_down, "s") #Cuando se presiona una tecla(s), usamos la funcion que le pasamos
wn.onkeypress(jugador2_up, "Up") #Lo mismo para el jugador 2, Up es la flecha del  teclado hacia arriba
wn.onkeypress(jugador2_down, "Down") #Lo mismo para el jugador 2, Down es la flecha del  teclado hacia abajo


#Bucle principal donde el juego va a ir corriendo, el primero en llegar a 15 puntos gana.
while marcador1 < 15 and marcador2 < 15:
    wn.update() #Para que se vaya actualizando
    
    #Le damos movimiento a la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    
    #Bordes arriba/abajo
    if pelota.ycor() > 290: #Esto es para que cuando llegue al tope de la ventana en la parte de arriba, la pelota se vuelva negativa y vaya hacia abajo
        pelota.dy *= -1
    
    if pelota.ycor() < -290: #Esto es para que cuando llegue al tope de la ventana en la parte de abajo, la pelota se vuelva positiva y vaya hacia arriba
        pelota.dy *= -1 
    
    #Bordes derecha/izquierda
    if pelota.xcor() > 390: #Esto es para que cuando llegue al lado izquierdo, la pelota vuelva al centro
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador1 += 1 #Le sumamos 1 al marcador cuando se realiza un punto
        pen.clear() #Borramos para que no se sobreescriban los puntos
        pen.write(f"Jugador1: {marcador1}      Jugador2: {marcador2}", align="center", font=("courier", 15, "normal")) #Actualizamos el marcador
        
    if pelota.xcor() < -390: #Esto es para que cuando llegue al lado derecho, la pelota vuelva al centro
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador2 += 1 #Le sumamos 1 al marcador cuando se realiza un punto
        pen.clear() #Borramos para que no se sobreescriban los puntos
        pen.write(f"Jugador1: {marcador1}      Jugador2: {marcador2}", align="center", font=("courier", 15, "normal")) #Actualizamos el marcador
        
    #Rebotes de la pelota con los cuadrados. Chequeo que la pelota este entre el rango x del jugador(cuadrado)
    #y chequeo que la pelota este entre el rango y del jugador(cuadrado), si esto pasa existe colision y cambio el sentido de la pelota.
    
    if ((pelota.xcor() > 340 and pelota.xcor() < 350) #Esto es para que cuando la pelota toca el cuadrado de la derecha(jugador2) la pelota rebote hacia el lado contrario
            and (pelota.ycor() < jugador2.ycor() + 50) 
            and (pelota.ycor() > jugador2.ycor() - 50)):
        pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350) #Esto es para que cuando la pelota toca el cuadrado de la izquierda(jugador1) la pelota rebote hacia el lado contrario
            and (pelota.ycor() < jugador1.ycor() + 50) 
            and (pelota.ycor() > jugador1.ycor() - 50)):
        pelota.dx *= -1