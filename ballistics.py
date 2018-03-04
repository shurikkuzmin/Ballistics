import numpy
import pylab


angle0 = 45.0*numpy.pi/180.0

x0 = 0
y0 = 0.0001
v0 = 10.0
dt = 0.005
alpha = 1.5
g = 10.0

traj_x = []
traj_y = []

x_old = x0
y_old = y0

vx_old = v0*numpy.cos(angle0)
vy_old = v0*numpy.sin(angle0)

while y_old > 0:
    traj_x.append(x_old)
    traj_y.append(y_old)

    vx_new = vx_old - alpha*vx_old*dt
    vy_new = vy_old - g*dt - alpha*vy_old*dt
    x_new = x_old + vx_old*dt
    y_new = y_old + vy_old*dt

    vx_old = vx_new
    vy_old = vy_new
    x_old = x_new
    y_old = y_new

pylab.plot(traj_x, traj_y)
pylab.show()