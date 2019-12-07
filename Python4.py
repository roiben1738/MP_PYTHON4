import matplotlib.pyplot as plot
import math as mt
import numpy as np
print(' ')
h = float(input('Input Height:'))
if h < 0:
    raise NameError('Invalid! Please input Height.')           
v = float(input('Input Velocity:'))
angle = float(input('Input Angle:'))
Ax = float(input('Input Horizontal Accelaration:'))
Ay = float(input('Input Vertical Accelaration:'))

if Ay == 0:
    raise NameError('Invalid! Zero vertical acceleration means no free-fall motion!')
        
def Python4(h, v, angle, Ax, Ay):
    
    FA = mt.radians(angle)
    FAS = mt.sin(FA)
    FAC = mt.cos(FA)
    
    T = (mt.sqrt(abs((v*FAS)**2-2*Ay*h)) - v*FAS)/Ay
    
    if T <= 0:
        T = (-mt.sqrt(abs((v*FAS)**2-2*Ay*h)) - v*FAS)/Ay

    t =  np.arange(0,T,0.005)
    xcomp = (v*FAC*t)+(1/2)*Ax*(t**2)
    ycomp = (h + v*FAS*t)+(1/2)*Ay*(t**2)
       
    plot.plot(xcomp,ycomp,'-')
    plot.grid()
    plot.xlabel('Horizontal Range')
    plot.ylabel('Height')
    plot.title('Trajectory')
    plot.show()

Python4(h, v, angle, Ax, Ay)