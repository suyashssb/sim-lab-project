
import scipy

a=scipy.array([3,5])

def F(z):
    f1=a[0]*z[0]+z[1]
    f2=a[1]*z[1]-a[0]
    f=scipy.array([f1,f2])
    return f
    
z1=scipy.array([1,2])
b=F(z1)[0]
print(b)


















