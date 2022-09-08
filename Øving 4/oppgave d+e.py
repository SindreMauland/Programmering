import math
def areal_av_sirkel(a):
    return(math.pi*a**2)
radius = float(input("Skriv inn radiusen til sirkelen: "))
print("Arealet av sirkelen er:",areal_av_sirkel(radius))