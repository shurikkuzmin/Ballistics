import numpy
import pylab

# Initial conditions
x0 = 0
y0 = 0.0001
dt = 0.005
alpha = 0.5
g = 10.0

# Input the length and velocity
length = float(input("Input the overal length: "))
v0 = float(input("Input the initial velocity: "))

# Guess the initial angle based on the motion without air friction
if g*length/(v0*v0) > 1:
    print("The input is not right. Please put a proper one!")
    exit(1)
else:
    angle0 = 0.5*numpy.arcsin(g*length/(v0*v0))
print("Initial angle in degrees is: ", angle0/numpy.pi*180.0)


x_old = x0
y_old = y0
angle_old = angle0

fig = pylab.figure(1)
fig.gca().set_aspect("equal")
for iter in range(0, 10):
    vx_old = v0*numpy.cos(angle_old)
    vy_old = v0*numpy.sin(angle_old)
    traj_x = []
    traj_y = []
    theor_x = []
    theor_y = []
    
    t = 0.0
    x_theor = x0
    y_theor = y0

    while y_old > 0:
        traj_x.append(x_old)
        traj_y.append(y_old)
        theor_x.append(x_theor)
        theor_y.append(y_theor)
        t = t + dt

        vx_new = vx_old - alpha*vx_old*dt
        vy_new = vy_old - g*dt - alpha*vy_old*dt
        x_new = x_old + vx_old*dt
        y_new = y_old + vy_old*dt

        # Analytical solution
        vx_theor = v0*numpy.cos(angle_old) * numpy.exp(-alpha*t)
        vy_theor = (v0*numpy.sin(angle_old) + g/alpha) * numpy.exp(-alpha*t) - g/alpha
        x_theor = x_theor + vx_theor*dt
        y_theor = y_theor + vy_theor*dt

        vx_old = vx_new
        vy_old = vy_new
        x_old = x_new
        y_old = y_new

    pylab.figure(1)
    pylab.plot(traj_x, traj_y)
    pylab.plot(theor_x, theor_y, "+")

    angle_new = angle_old - (x_old-length)/(2.0*v0*v0*numpy.cos(2.0*angle_old)/g)
    
    print("Prediction and length = ",x_old, length)
    print("Old angle = ", angle_old*180.0/numpy.pi)
    print("Predicted angle = ", angle_new*180.0/numpy.pi)
    x_old = x0
    y_old = y0
    angle_old = angle_new

pylab.show()