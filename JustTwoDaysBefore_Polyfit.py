
from numpy import *
from matplotlib.pyplot import *
from scipy.optimize import *
from scipy.interpolate import *  # For polyfit

x=array([1,2,3,4,5,6,7,8,9,10,11]) 
y=array([-1,3,7,34,67,167,55,100,19,-2,-22])

p1=polyfit(x,y,1)
p2=polyfit(x,y,2)
p3=polyfit(x,y,8)

xp=linspace(1,11,100)
y1=polyval(p1,xp)
y2=polyval(p2,xp)
y3=polyval(p3,xp)

plot(x,y,'o')
plot(xp,y1,'r-')
plot(xp,y2,'m-')
plot(xp,y3,'b--')

y1fit=polyval(p1,x)

y1res=y-y1fit
ssy1res=sum(power(y1res,2))
sstotal=len(y)*var(y)
Rsquared=1-(ssy1res/sstotal)
print(Rsquared)



m=exp(1)
print(m)






































