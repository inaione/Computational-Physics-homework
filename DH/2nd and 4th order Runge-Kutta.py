import numpy as np
import matplotlib.pyplot as plt


# 准备坐标轴
plt.figure(num=1, figsize=(8, 8))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 画太阳
plt.scatter(0, 0, s=200, marker=(20, 1), color='y')

# 4th-order Runge-Kutta分析
x = []
y = []
dt = 0.00125
e = 0.8   # 设置离心率
pos = [[0], [1-e]]
v1 = [-np.sqrt((1+e)/(1-e)), 0]

def R(m,n):
    return (m ** 2 + n ** 2) ** 0.5

for index in range(5000):
    r1 = R(pos[0][index], pos[1][index])
    a1 = [-pos[0][index] / (r1 ** 3), -pos[1][index] / (r1 ** 3)]

    v2 = [v1[0] + a1[0]*dt/2, v1[1] + a1[1]*dt/2]
    pos2 = [pos[0][index] + v1[0]*dt/2, pos[1][index] + v1[1]*dt/2]
    r2 = R(pos2[0], pos2[1])
    a2 = [-pos2[0] / (r2 ** 3), -pos2[1] / (r2 ** 3)]

    v3 = [v1[0] + a2[0]*dt/2, v1[1] + a2[1]*dt/2]
    pos3 = [pos[0][index] + v2[0]*dt/2, pos[1][index] + v2[1]*dt/2]
    r3 = R(pos3[0], pos3[1])
    a3 = [-pos3[0] / (r3 ** 3), -pos3[1] / (r3 ** 3)]

    v4 = [v1[0] + a3[0]*dt, v1[1] + a3[1]*dt]
    pos4 = [pos[0][index] + v3[0]*dt/2, pos[1][index] + v3[1]*dt/2]
    r4 = R(pos4[0], pos4[1])
    a4 = [-pos4[0] / (r4 ** 3), -pos4[1] / (r4 ** 3)]

    slope_v = [(v1[0] + 2*v2[0] + 2*v3[0] + v4[0])/6, (v1[1] + 2*v2[1] + 2*v3[1] + v4[1])/6]
    slope_a = [(a1[0] + 2*a2[0] + 2*a3[0] + a4[0])/6, (a1[1] + 2*a2[1] + 2*a3[1] + a4[1])/6]

    pos_x_next = pos[0][index] + slope_v[0] * dt
    pos_y_next = pos[1][index] + slope_v[1] * dt

    v1[0] += slope_a[0]*dt
    v1[1] += slope_a[1]*dt

    pos[0].append(pos_x_next)
    pos[1].append(pos_y_next)

x.append(pos[0])
y.append(pos[1])

#2nd-order Runge-Kutta 分析
x0 = []
y0 = []

pos = [[0], [1-e]]
v = [-np.sqrt((1+e)/(1-e)), 0]
for index in range(5500):
    pos_next_half = [v[0]*dt/2 + pos[0][index], v[1]*dt/2 + pos[1][index]]
    r = np.sqrt(pos[0][index] ** 2 + pos[1][index] ** 2)
    r_half = (pos_next_half[0] ** 2 + pos_next_half[1] ** 2) ** 0.5
    a = [-pos[0][index] / (r ** 3), -pos[1][index] / (r ** 3)]
    a_next_half = [-pos_next_half[0] / (r_half ** 3), -pos_next_half[1] / (r_half ** 3)]
    v_next_half = [v[0] + (dt/2)*a[0], v[1] + (dt/2)*a[1]]
    pos_x_next = pos[0][index] + v_next_half[0]*dt
    pos_y_next = pos[1][index] + v_next_half[1]*dt
    pos[0].append(pos_x_next)
    pos[1].append(pos_y_next)
    v[0] += a_next_half[0]*dt
    v[1] += a_next_half[1]*dt
x0.append(pos[0])
y0.append(pos[1])

# 画出曲线
plt.plot(x[0], y[0], 'b',label="4th-order Runge-Kutta")
plt.plot(x0[0], y0[0], 'y',label="2nd-order Runge-Kutta")

# 加上列表名
plt.title('4th-order and 2nd-order Runge-Kutta method for orbit problem(e = 0.8)')
plt.legend(loc='best')
plt.xlim(-2.5, 2.5)
plt.ylim(-2.0, 2.0)
plt.show()
