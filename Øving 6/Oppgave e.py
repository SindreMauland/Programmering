from matplotlib import pyplot as plt
import numpy as np
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
plt.plot(t,htotal)
plt.show()

f.close()