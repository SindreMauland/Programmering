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

ar = np.array(hastighet1)
ar1 = np.array(hastighet2)
ar2 = total(ar,ar1)
print(ar2)
f.close()