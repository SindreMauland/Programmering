
import random
def avstand():
    return(x*x+y*y)**0.5

i_firkant = 0


i_sirkel = 0
def inni_sirkel():
    if (avstand()<=1):
        global i_sirkel
        i_sirkel+=1
koordinater = int(input("Skriv inn antall koordinater du vil skjekke om er innenfor sirkelen: "))
for i in range(koordinater):
    x = random.random()
    y = random.random()
    avstand()
    i_firkant+=1
    inni_sirkel()

print(4*i_sirkel/i_firkant)    