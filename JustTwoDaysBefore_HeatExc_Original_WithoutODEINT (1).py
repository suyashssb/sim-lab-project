
import scipy
from scipy.optimize import fsolve

ma=1
mb=2
Tain=400
Tbin=300
U=100
P=1
L=10
ka=-(U*P/ma)
kb=-(U*P/mb)
n=10

def cpa(T):
    f=4000+10*T+0.01*T*T
    return f
def cpadT(T):
    f=4000*T+10*T*T/2+0.01*T*T*T/3
    return f
    
def cpb(T):
    f=3000+5*T+0.02*T*T
    return f
def cpbdT(T):
    f=3000*T+5*T*T/2+0.02*T*T*T/3
    return f
    
Ta0=Tain
Tb0=Tain-0.0001
Tbn=329
e=Tbn-Tbin

while e<=-0.0001 or e>=0.0001:
    Ta=Ta0
    Tb=Tb0
    for i in range(n-1):
        dTadx=(ka/cpa(Ta))*(Ta-Tb)
        Ta=Ta+(dTadx*L/n)
        dTbdx=(kb/cpb(Tb))*(Ta-Tb)
        Tb=Tb+(dTbdx*L/n)
    Tan=Ta
    Tbn=Tb
    Ta0=Ta0
    Tb0=Tb0
    e=Tbn-Tbin
    if e<=-0.0001 or e>=0.0001:
        Tb0=Tb0-0.0001
    else:
        print("The inlet Ta is ")
        print(Ta0)
        print("The outlet Ta is ")
        print(Tan)
        print("The outlet Tb is ")
        print(Tb0)
        print("The inlet Tb is ")
        print(Tbn)
        break

Ha=ma*(cpadT(Ta0)-cpadT(Tan))
Hb=mb*(cpbdT(Tb0)-cpbdT(Tbn))
ef=Ha-Hb
print("For number of steps ")
print(n)
print("using Euler, ")
print("The error in enthalpy is ")
print(ef)

