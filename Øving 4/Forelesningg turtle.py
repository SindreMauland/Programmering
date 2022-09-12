import turtle
t=turtle.Turtle()
antall = int(input("Hvor mange diamanter vil du ha? "))
a=10
x=1
t.speed(0)
def c():
    t.left(135)
    t.penup()
    t.forward(10)
    t.pendown()
    t.right(135)
def z():

    t.penup()
    t.forward(20)
    t.pendown()
    t.right(45) 
z() 
def diamant():
    for i in range(4):
        t.forward(14.14*x)
        t.right(90)
for i in range (antall):
    diamant()
    x+=1

    c()

turtle.done()