from frederiquefunctions import*
turtle.bgcolor("black")
bob.speed(0)


bob.right(90)
bob.color("red")
for times in range(100):
    bob.stamp()
    bob.circle(times*10)
    bob.stamp()
    
bob.right(180)
bob.color("cyan")
for times in range(100):
    bob.circle(times*10)
    bob.stamp()

bob.left(90)
bob.color("magenta")
for times in range(100):
    bob.stamp()
    bob.circle(times*10)
    bob.stamp()

bob.left(180)
bob.color("magenta")
for times in range (100):
    bob.stamp()
    bob.circle(times*10)
    bob.stamp()


