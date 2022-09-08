
import random

i_firkant = 0
i_sirkel = 0
koordinater = int(input("Skriv inn antall koordinater du vil skjekke om er innenfor sirkelen: "))
for i in range(koordinater):
    x = random.random()
    y = random.random()
    d = (x*x+y*y)**0.5
    i_firkant+=1
    if (d<=1):

        i_sirkel+=1

print(4*i_sirkel/i_firkant)    
