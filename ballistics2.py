import numpy
import pylab
import scipy.optimize

alpha = 0.25
g = 10.0

# Input the length and velocity
length = float(input("Input the overal length: "))
v0 = float(input("Input the initial velocity: "))

# Guess the initial angle based on the motion without air friction
if g*length/(v0*v0) > 1:
    print("The input is not right. Please put a proper one!")
    exit(1)

angle_init = 0.5*numpy.arcsin(g*length/(v0*v0))
time_init = 2.0*v0*numpy.sin(angle_init)/g
print("Initial angle in degrees is: ", angle_init/numpy.pi*180.0)
print("Initial time is: ", time_init)

# Theoretical equations 
#vx = v0*numpy.cos(angle_old) * numpy.exp(-alpha*t)
#vy = (v0*numpy.sin(angle_old) + g/alpha) * numpy.exp(-alpha*t) - g/alpha
#x = v0*numpy.cos(angle0)/alpha * (1.0 - numpy.exp(-alpha*t))
#y = (v0*numpy.sin(angle0) + g/alpha)/alpha * (1.0-numpy.exp(-alpha*t)) - g*t/alpha

def fun(args):
    x = v0*numpy.cos(args[0])/alpha * (1.0 - numpy.exp(-alpha*args[1])) - length
    y = (v0*numpy.sin(args[0]) + g/alpha)/alpha * (1.0-numpy.exp(-alpha*args[1])) - g*args[1]/alpha
    return [x,y]

angle, time=scipy.optimize.broyden1(fun, [angle_init, time_init])
print("Final angle in degrees = ", angle/numpy.pi*180.0)
print("Time = ", time)

# Final trajectory
t = numpy.linspace(0.0, time, 101)
traj_x = v0*numpy.cos(angle)/alpha * (1.0 - numpy.exp(-alpha*t)) 
traj_y = (v0*numpy.sin(angle) + g/alpha)/alpha * (1.0-numpy.exp(-alpha*t)) - g*t/alpha

pylab.plot(traj_x, traj_y)
pylab.show()
