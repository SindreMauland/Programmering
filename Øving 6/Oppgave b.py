
import math
def areal_av_sirkel(a):
    return(math.pi*a**2)
radius = 0.5

def energiproduksjon_turbin(turbin_effekt,tetthet,areal,strøm):
    return(0.5*turbin_effekt*tetthet*areal*strøm)
a=0.3
b=1000
c=areal_av_sirkel(radius)
d=areal_av_sirkel(radius)

energiproduksjon_turbin(a,b,c,d)