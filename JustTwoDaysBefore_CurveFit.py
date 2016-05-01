# -*- coding: utf-8 -*-
"""
Created on Sun May 01 19:51:19 2016

@author: ASHWIN KANE
"""

from numpy import *
from matplotlib.pyplot import *
from scipy.optimize import *
from scipy.interpolate import *

xdata=array([1,2,3,4,5,6,7,8])
def f(x,a,b,c,d):
    f=a+b*e**x+c*x**2+d*log(x)
    return f
ydata=f(xdata,56,0.05,0.45,277)
print(ydata)
ydata=ydata+1

popt,pcov=curve_fit(f,xdata,ydata)
print(popt)















































