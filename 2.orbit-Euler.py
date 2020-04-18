import numpy as np
import matplotlib.pyplot as plt

plt.figure(num=1,figsize=(8,8))

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.scatter(0,0,s=250,marker=(20,1),color="y")

dt=[0.0125,0.05,0.1,0.15]
x=[]
y=[]
for i in range(4):
    pos=[[0],[1]]                             #position list which include x[]list and y[]list
    v=[-1,0]
    for index in range(300):
        r=np.sqrt(pos[0][index]**2+pos[1][index]**2)
        a_abs=1/(r**2)
        a=[a_abs*(-pos[0][index])/r,a_abs*(-pos[1][index])/r]
        pos[0].append(v[0]*dt[i]+pos[0][index])
        pos[1].append(v[1]*dt[i]+pos[1][index])
        v[0]+=a[0]*dt[i]
        v[1]+=a[1]*dt[i]
        if index*dt[i]>=5:                    #lenth of curve 
            break
    x.append(pos[0])
    y.append(pos[1])

plt.plot(x[0],y[0],'b',label='dt=0.0125')
plt.plot(x[1],y[1],'k',label='dt=0.05')
plt.plot(x[2],y[2],'y',label='dt=0.1')
plt.plot(x[3],y[3],'r',label='dt=0.15')

theta=np.linspace(0,2*np.pi,360)
m=np.cos(theta)
n=np.sin(theta)
plt.plot(m,n,'k')

plt.legend(loc='best')
plt.title('Euler method for orbit')
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.axis('equal')

plt.show()
