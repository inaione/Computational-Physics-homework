import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

i=np.linspace(-20,0,50)
h=pow(10,i)
x0=1.2
ab_error=abs(np.cos(x0)-(np.sin(x0+h)-np.sin(x0))/h)

plt.autoscale()
plt.title("Round errors")
plt.loglog(h,ab_error,'b')
plt.loglog(h,np.sin(x0)*h/2,'r',linestyle='-.')
plt.scatter(h,ab_error,marker='o',s=8)
plt.ylabel("Absolute error",fontsize=15)
plt.xlabel("h",fontsize=15)
plt.ylim(10**-15,1)
plt.xlim(10**-20,1)
plt.show()
