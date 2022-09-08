
import turtle
window = turtle.Screen()
window.bgcolor("black")

a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()
d=turtle.Turtle()
e=turtle.Turtle()


def t(y):
    y.speed(0)
    y.hideturtle()
    y.color("yellow")
t(a)
t(b)
t(c)
t(d)
t(e)

b.right(72)
c.right(144)
d.right(216)
e.right(288)

def stjerne(x):   
    x.forward(6)
    x.back(6)
    x.right(30)



def spiral(t):
    t.left(30)
    t.penup()
    t.forward(20)
    t.pendown()
    for a in range(12):
        stjerne(t)
    t.right(5)
def snurr(l):
    spiral(l)
    stjerne(l)

stjerner=int(input("Hvor mange stjerner på hver arm vil du ha? "))

for i in range(stjerner):
    snurr(a)
    snurr(b)
    snurr(c)
    snurr(d)
    snurr(e)



turtle.done()