from sys import _enablelegacywindowsfsencoding


alder = float(input("Hvor gammel er du? "))


if alder<4:
    print("Du kommer inn gratis!")
if (4<=alder) and (alder<=16):
    print("Det koster 45 kroner!")
if (17<=alder) and (alder<=66): 
    student = input("Er du student? ")  
    if (student=="Ja" or student=="ja"):
        print("Det koster 50 kroner")
    else:
        print("Det koster 90 kroner")
if alder>=67:
    print("Det koster 50 kroner")
