
import scipy
from scipy.optimize import fsolve

PcA=8.084*10**6 # in Pascal
TcA=512.5 # Kelvin

PcB=63*10**5 # Pascal
TcB=514 # Kelvin
R=8.314472
Pc=scipy.array([PcA,PcB])
Tc=scipy.array([TcA,TcB])
def a(Pc,Tc):
    a1=(0.42748*R**2*Tc[0]**2.5)/Pc[0]
    a2=(0.42748*R**2*Tc[1]**2.5)/Pc[1]
    a=scipy.array([a1,a2])
    return a
def b(Pc,Tc):
    b1=(0.08664*R*Tc[0])/Pc[0]
    b2=(0.08664*R*Tc[1])/Pc[1]
    b=scipy.array([b1,b2])
    return b
print('b value is')
print(b(Pc,Tc))



































