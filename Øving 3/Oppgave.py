import random
vinn_uendret=0
vinn_endret=0

for i in range(1000):
    gjett = random.randint(1,3)
    gevinst = random.randint(1,3)
    d = [1,2,3]
    d.remove(gjett)
    if (gjett!=gevinst):
        d.remove(gevinst)
    vert_valg = random.choice(d)

    if (gjett==gevinst):
        vinn_uendret+=1
print(vinn_uendret)
for i in range(1000):
    gjett = random.randint(1,3)
    gevinst = random.randint(1,3)
    d = [1,2,3]
    d.remove(gjett)
    if (gjett!=gevinst):
        d.remove(gevinst)
    vert_valg = random.choice(d)

    if (gjett!=gevinst):
        vinn_endret+=1
print(vinn_endret)