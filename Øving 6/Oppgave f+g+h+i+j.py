from matplotlib import pyplot as plt
import numpy as np
import math
def areal_av_sirkel(a):
    return(math.pi*a**2)
radius = 0.5

def energiproduksjon_turbin(turbin_effekt,tetthet,areal,strøm):
    return(0.5*turbin_effekt*tetthet*areal*strøm)
a=0.3
b=1000
c=areal_av_sirkel(radius)




f = open("Øving 6\\tidevannsdata_csv.txt","r")
tidspunkt =[]
hastighet1 =[]
hastighet2=[]
def total(retning1, retning2):
    return(retning1**2+retning2**2)**0.5

for i in f:
    try:
        split = i.split(";")
        tidspunkt.append(float(split[0]))
        hastighet1.append(float(split[1]))
        hastighet2.append(float(split[2]))
    except (ValueError, TypeError):
        continue
t = np.array(tidspunkt)
h1 = np.array(hastighet1)
h2 = np.array(hastighet2)
htotal = total(h1,h2)

effekt = np.array(energiproduksjon_turbin(a,b,c,htotal))
print(effekt)
plt.plot(t,effekt)
plt.show()
gjennomsnitt = np.average(htotal)
snittstrøm_effekt = energiproduksjon_turbin(a,b,c,gjennomsnitt)
g_effekt = np.average(effekt)
print("Gjennomsnittlig Vannstrøm: ",gjennomsnitt)
print("Effekt basert på snittstrøm: ",snittstrøm_effekt)
print("Gjennomsnittlig effekt: ",effekt)

f.close()