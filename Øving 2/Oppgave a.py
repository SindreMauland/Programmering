temp1 = float(input("Hvor mange grader var det om morgenen? "))
temp2 = float(input("Hvor mange grader var det om kl 16? "))
f1 = temp2-temp1
if temp2 > temp1: 
    print(("Temperaturen har steget med: ")+str(f1))
if temp2 < temp1: 
    print("Temperaturen har sunket med: "+str(-f1))
if temp1==temp2:
    print("Temperaturen har ikke endret seg!")
