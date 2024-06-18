#Hola


import turtle as turtle
import os

playerAscore = 0
playerBscore = 0

window=turtle.Screen()
window.title("Mi primerPong")
window.bgcolor("black") 
window.setup(width=800,height=600)
window.tracer(0)

#crear raqueta izq
playerA=turtle.Turtle()
playerA.speed(0)
playerA.shape("square")
playerA.color("white")
playerA.shapesize(stretch_wid=5,stretch_len=1)
playerA.penup()
playerA.goto(-350,0)

#crear raqueta der
playerB=turtle.Turtle()
playerB.speed(0)
playerB.shape("square")
playerB.color("white")
playerB.shapesize(stretch_wid=5,stretch_len=1)
playerB.penup()
playerB.goto(350,0)

#crear pelota
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=0.5

#Tabla de puntuacion
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0",align="center",font=("Courier",24,"normal"))

#mover player a
def playerAup():    
    y=playerA.ycor()
    y+=20
    playerA.sety(y)

def playerAdown():
    y=playerA.ycor()
    y-=20
    playerA.sety(y)

#mover player b
def playerBup():
    y=playerB.ycor()
    y+=20
    playerB.sety(y)

def playerBdown():
    y=playerB.ycor()
    y-=20
    playerB.sety(y)

#Controles
window.listen()
window.onkeypress(playerAup,"w")
window.onkeypress(playerAdown,"s")
window.onkeypress(playerBup,"Up")
window.onkeypress(playerBdown,"Down")

while True:
    window.update()

    #mover la bola
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #bordes
    if  ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if  ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    
    if  ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        playerAscore+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(playerAscore,playerBscore),align="center",font=("Courier",24,"normal"))

    if  ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        playerBscore+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(playerAscore,playerBscore),align="center",font=("Courier",24,"normal"))

#colisiones
        # Verifica la colision de la bola con la raqueta derecha
    if ball.distance(playerB) < 50 and ball.xcor() > 340:
        ball.setx(340) #coloca la pelota en el borde de la raqueta
        ball.dx *= -1 #invierte la direccion de la bola
        os.system("afplay boing.wav&") #reproduce un sonido

    if ball.distance(playerA) < 50 and ball.xcor() < -340:
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay boing.wav&")
    
                                                     
