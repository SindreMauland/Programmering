
num2 = 0
while True:
    num1 = float(input("Skriv inn tall et tall: "))
    if num1<0:
        print("Tallet du valgte er negativt! Start på nytt!")
        break
    if num2>num1 and num2>0:
        forskjell = num2-num1
        print("Tallet er "+str(forskjell)+(" mindre enn det forrige tallet"))
    if num1>num2 and num1>0:
        forskjell1 = num1-num2
        print("Tallet er "+str(forskjell1)+(" større enn det forrige tallet"))
    num2 = num1


