import numpy as np
import matplotlib.pyplot as plt

def f(num_):
    plt.figure(num=num_*10,figsize=(8,8))

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    plt.scatter(0,0,s=250,marker=(20,1),color='y')

    dt=0.0125
    e=num_

    posEC=[[0],[1*(1-e)]]
    v=[-np.sqrt((1+e)/(1-e)),0]
    for index in range(500):
        r=np.sqrt(posEC[0][index]**2+posEC[1][index]**2)
        a=[-posEC[0][index]/(r**3),(-posEC[1][index])/(r**3)]
        v[0]+=a[0]*dt
        v[1]+=a[1]*dt
        posEC[0].append(posEC[0][index]+v[0]*dt)
        posEC[1].append(posEC[1][index]+v[1]*dt)         #Euler-Cromer method
    
    posRK=[[0],[1*(1-e)]]
    v=[-np.sqrt((1+e)/(1-e)),0]
    for index in range(500):
        R=np.sqrt(posRK[0][index]**2+posRK[1][index]**2)
        a=[-posRK[0][index]/(R**3),-posRK[1][index]/(R**3)]     
        v_mid=[v[0]+a[0]*(dt/2),v[1]+a[1]*(dt/2)]
        r_mid=[posRK[0][index]+v[0]*(dt/2),posRK[1][index]+v[1]*(dt/2)]
        R_mid=np.sqrt(r_mid[0]**2+r_mid[1]**2)
        a_mid=[-r_mid[0]/(R_mid**3),-r_mid[1]/(R_mid**3)]
        v[0]+=a_mid[0]*dt
        v[1]+=a_mid[1]*dt
        posRK[0].append(posRK[0][index]+v_mid[0]*dt)
        posRK[1].append(posRK[1][index]+v_mid[1]*dt)

    plt.plot(posEC[0],posEC[1],'y',linewidth=1.0,label='Euler-Cromer method for Elliptical Orbits')
    plt.plot(posRK[0],posRK[1],'b',linewidth=1.0,label='2nd-Runge-Kutta for Elliptical Orbits')

    plt.legend(loc='upper left')
    plt.title('2nd-order Runge-Kutta vs Euler-Cromer(e=%f)'%e)
    plt.xlim(-2,2)
    plt.ylim(-3,3)
    plt.axis('equal')

for i in range(0,10,2):
    f(i/10)
    
plt.show()
