
import scipy
from scipy.optimize import fsolve
x=1
b=2
a=b
while a!=9:
    x=x
    b=x
    for i in range(5):
        b=b+1
    a=b
    if a!=9:
        x=x+1
    else:
        print("the soln is ")
        print(x)
        break

                
    
    
    








































