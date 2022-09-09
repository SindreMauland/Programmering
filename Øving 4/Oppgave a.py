import turtle
t=turtle.Turtle()
t.speed(0)
a=5
antall = int(input("Hvor mange linjer skal spiralen ha? "))
for i in range(antall):
    t.forward(a)
    t.right(90)
    a+=5
turtle.done()