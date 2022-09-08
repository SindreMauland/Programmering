import turtle


a = turtle.Turtle()
størrelse = 10
a.speed(9)
while True:
    a.circle(størrelse)
    a.right(90)
    a.circle(størrelse)
    a.right(90)
    a.circle(størrelse)
    a.right(90)
    a.circle(størrelse)
    a.right(90)    
    størrelse +=10
    a.right(10)
