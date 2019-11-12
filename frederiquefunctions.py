import turtle
bob=turtle.Turtle()
ali=turtle.Turtle()
def polygon(sides,distance,c):
    bob.color(c)
    angle=360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)

    bob.end_fill()
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    
def star(distance,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.left(-144)
        bob.end_fill()

def fadingtriangle():
    for times in range(50):
        c=(250-times*5,250-times*5,0)
        polygon(3,450-times*8,c)
 


def explosion(distance,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(distance)
        bob.left(135)
    bob.end_fill()

def figure1(distance,color):
    bob.color(color)
    bob.begin_fill()
    bob.circle(10)
    bob.end_fill()
    bob.forward(distance)
    bob.begin_fill()
    bob.circle(10)
    bob.end_fill()
    bob.left(45)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(45)
    bob.begin_fill()
    bob.circle(10)
    bob.end_fill()
    bob.forward(distance)
    bob.begin_fill()
    bob.circle(10)
    bob.end_fill()
    bob.end_fill()

def monster(distance,color):
    bob.color(color)
    bob.begin_fill()
    bob.left(90)
    bob.forward(100)
    bob.circle(50)
    bob.right(90)
    bob.forward(-100)
    bob.right(90)
    bob.forward(100)
    bob.left(125)
    bob.forward(30)
    bob.right(90)
    bob.forward(35)
    bob.left(90)
    bob.forward(35)
    bob.right(90)
    bob.forward(35)
    bob.left(135)
    bob.forward(35)
    bob.end_fill()

def tile():
    for times in range(4):
        polygon(3,150,"black")
        bob.forward(150)
        polygon(3,150,"black")
        bob.forward(150)
        polygon(3,150,"black")
        bob.forward(150)
        polygon(3,150,"black")
        bob.forward(150)
        bob.left(90)


def curve(distance,angle):
    for times in range(20):
        bob.width(times)
        bob.forward(distance)
        bob.left(angle)

def spiralsq(distance,face):
    for time in range(20):
        bob.forward(distance,times*10)
        bob.left(face)

def sqspin():
    bob.speed(9)
    turtle.bgcolor("white")
    for times in range(60):
        c=(250-times*255-times*5,0)
        bob.color("white")
        bob.forward(times*5)
        bob.color("brown")
        bob.stamp()
        bob.forward(times*5)
        bob.color("black")
        bob.stamp()
        bob.left(92)
