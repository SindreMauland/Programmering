import turtle
import sys
kanter = int(input("Skriv inn hvor mange kanter du vil mangekanten skal ha"))
vinkel = 360/kanter
a = turtle.Turtle()

for i in range(kanter):
    if kanter<3:
        print("For få kanter")
        sys.exit()
        break
    a.forward(100)
    a.right(vinkel)


turtle.done()