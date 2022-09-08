import math
def areal_av_sirkel(a):
    return(math.pi*a**2)
radius = float(input("Skriv inn radiusen til sirkelen: "))

def energiproduksjon_turbin(turbin_effekt,tetthet,areal,strøm):
    return(0.5*turbin_effekt*tetthet*areal*strøm)
a=0.3
b=1000
c=areal_av_sirkel(radius)
d=float(input("Hvor mye strøm er det: "))
print(energiproduksjon_turbin(a,b,c,d))
