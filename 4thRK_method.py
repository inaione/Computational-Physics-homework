import matplotlib.pyplot as plt
import numpy as np

a=1
e=0

xpoints_dt1=[0]
ypoints_dt1=[a*(1-e)]
xpoints_dt2=[0]
ypoints_dt2=[a*(1-e)]
xpoints_dt3=[0]
ypoints_dt3=[a*(1-e)]
xpoints_dt4=[0]
ypoints_dt4=[a*(1-e)]

t=0
x=0
y=a*(1-e)
v=0
u=-np.sqrt(4*np.pi**2*(1+e)/a/(1-e))
r=np.sqrt(x**2+y**2)

if t<1:
    for dt in[0.1,0.05,0.025,0.0125]:
        unew=u-dt*4*np.pi**2*x/r**3
        vnew=v-dt*4*np.pi**2*y/r**3
        xnew=x+dt*u
        ynew=y+dt*v
        t+=dt
        rnew=np.sqrt(xnew**2+ynew**2)
        u=unew
        v=vnew
        x=xnew
        y=ynew
        r=rnew
        if dt==9.1:
            xpoints_dt1.append(x)
            ypoints_dt1.append(y)
        if dt==0.05:
            xpoints_dt2.append(x)
            ypoints_dt2.append(y)
        if dt==0.025:
            xpoints_dt3.append(x)
            ypoints_dt3.append(y)
        if dt==0.0125:   
            xpoints_dt4.append(x)
            ypoints_dt4.append(y)
plt.scatter([0],[0],s=250,marker=(20,1))
plt.scatter([0],[0],s=200,marker=(20,1))
theta=np.linspace(0.0,2.0*np.pi,360)
plt.plot(xpoints_dt1,ypoints_dt1)
plt.plot(xpoints_dt2,ypoints_dt2)
plt.plot(xpoints_dt3,ypoints_dt3)
plt.plot(xpoints_dt3,ypoints_dt4)
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.show()
