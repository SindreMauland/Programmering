
bStart = input("Hvor mye starter befolkningen på? ")
bStart_tall = float(bStart)
o = input("Hvor mange prosent øker befolkningen årlig? ")
o_tall = float(o)
a = input("Hvor mange år øker befolkningen? ")
a_tall = float(a)


Svar = (bStart_tall*(1.0+((o_tall)/(100)))**a_tall)
print(Svar)