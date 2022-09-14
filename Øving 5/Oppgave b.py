def temperatur():
    while True:
        try:
            temp1 = float(input("Hvor mange grader var det om morgenen? "))
            temp2 = float(input("Hvor mange grader var det om kl 16? "))
        except ValueError:
            print("Det du skrev inn ble ikke akseptert. Prøv igjen!")
            continue
        f1 = temp2-temp1
        if temp2 > temp1: 
            print(("Temperaturen har steget med: ")+str(f1))
        elif temp2 < temp1: 
            print("Temperaturen har sunket med: "+str(-f1))
        elif temp1==temp2:
            print("Temperaturen har ikke endret seg!")
print(temperatur())