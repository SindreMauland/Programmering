

def tall_positivt_negativt(a):
    if a>b:
        print("Tallet har økt med:",abs(a)-abs(b))
    else:
        print("Tallet har sunket med:", abs(b)-abs(a))
b =0
while True:
    a=float(input("Skriv inn et tall: "))
    if  a<0:
        break
    tall_positivt_negativt(a)
    b=a