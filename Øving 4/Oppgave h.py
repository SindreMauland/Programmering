from asyncio.windows_events import NULL


def fot_meter(f):
    return(f*0.3048)
fot= None
while True:
    fot=float(input("Hvor mange fot? "))
    if fot==0:
        break
    print(abs(fot_meter(fot)))