f = open("Øving 8\\befolkning_tabell_csv.txt","r")
g = open("Øving 8\\areal_tabell_csv.txt","r")

l={}
z={}
class land:
    def __init__(self, navn, befolkning=0, areal=0):
        self.navn = navn
        self.befolkning = befolkning
        self.areal = areal
    def __str__(self):
        return(f"Navn: {self.navn} Befolkning: {self.befolkning} Areal: {self.areal}")
    def __repr__(self):
        return(f"Navn: {self.navn} Befolkning: {self.befolkning} Areal: {self.areal}")
    def befolkningstetthet(self, befolkning, areal):
        return(befolkning/areal)


n=0

for i in f:
    strip = i.strip()
    split = i.split(";")
    e = land(navn=split[0],**l)
"""     l=land(split[0], float(split[1]), 0) """

print(e.navn,e.befolkning,e.areal)

        


print(l)

land1 = land("Norge", 5000000, 10000000)
land2 = land("Spania", 3000000, 20000000)

def h_befolkning(a,b,c,d):
    if a>b:
        print("Befolkningen er høyest i", c)
        print("Befolkningen i",c,"er", a)
    else:
        print("Befolkningen er høyest i", d)
        print("Befolkningen i",d,"er", b)

print(h_befolkning(land1.befolkning, land2.befolkning,land1.navn,land2.navn))
       
f.close()