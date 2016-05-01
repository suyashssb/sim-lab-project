import scipy
from scipy.optimize import fsolve

def f(x):
    f1=x**2+2*x+1
    f2=x**2+5*x+6
    f=scipy.array([f1,f2])
    return f

xg=0
a=f(x)[1]
x=fsolve(a,xg)
print(x)








