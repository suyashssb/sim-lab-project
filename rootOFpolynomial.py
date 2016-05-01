
def f(x):
    y=x**2+2*x+1
    return y
    
x0=-19
y0=f(x0)
while y0 != 0:
    x1=x0+0.001
    y1=f(x1)
    if y1==0:
        print('answer for root is' )
        print(x1)
        break
    else:
        x0=x1
    










































