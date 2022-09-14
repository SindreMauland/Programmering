



f = open("Øving 5\max_vind_sola_enkelttall.txt","r")
liste = []
num2=0
sum =0
def gjennomsnitt(a,b):
    return(a/b)
antall =0
for i in f:

    liste.append(float(i))
    num1 = float(i)
    if num1>num2:
        num2=num1
    sum+=num1
    antall+=1

print("Antall målinger som ble gjort var:", antall)
print("Gjennomsnittlig vind var på:",gjennomsnitt(sum,antall) )
    
print("Høyeste vindmålingen var på:",num2)
f.close()