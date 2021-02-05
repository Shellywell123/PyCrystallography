from PyCrystallography.lattice import make_lattice_2d
from PyCrystallography.unit_cell import primitive_cell_2d

import numpy as np
import matplotlib
try:
    matplotlib.use('TkAgg')
except:
    pass
    
import matplotlib.pyplot as plt


# make lattice
plt.figure('Xray-Diffraction')
primitive_cell_2d = primitive_cell_2d('square')
lattice_points = make_lattice_2d(primitive_cell_2d,depth=15)


#print(lattice_points)

# fire particles

# angle fro surface norm (degrees)
theta = 40

#cant be zero min = 1
num_of_particles = 10

#cant be zero min = 1
spread = 1

#compute angles and collisions

def braggs_law(n,lambd,theta):
    """
    return lattic distancing
    """
    d = n*lambd/(2*np.sin(theta))

    return d

def collisions(lattice_points,particle_num,theta,spread):
    """
    boolean colision indicator
    """
    for lattice_point in lattice_points:

        x = lattice_point[0]
        y = lattice_point[1]

        d_x = (particle_num+1/num_of_particles)*spread
        c = d_x*np.tan(theta)

        y_calc = np.tan(theta)*x + c

        #print (c)

        #detection sensitivity
        ds = 0.4
        if (y_calc -ds< y < y_calc + ds):
            print('collision')
            print(y)
            return y_calc

    return None

# reflect paricles
#plt.plot()
#collisions(lattice_points,num_of_particles,theta,spread)

theta = np.radians(theta)
x_origin = -1
y_origin = -10.5

canvas_size = 16

for i in range(0,num_of_particles):

    x1 = x_origin + (i+1/num_of_particles)*spread
    y1 =y_origin

    if collisions(lattice_points,i,theta,spread):
        y2 = collisions(lattice_points,i,theta,spread)    
        d_x = (i+1/num_of_particles)*spread
        c = d_x*np.tan(theta)   
        x2 = (y2 - c)/np.tan(theta) #+ 
        # plot reflected particle
        x3 = x_origin + canvas_size
        m = (y2-y1)/(x2-x1)

        #need to fgure out c
        c = 0
        y3 = -m*x3 + c
        plt.plot([x1,x2,x3],[y1,y2,y3]) 
    else:
        y2 = y_origin + canvas_size
        x2 = (y2)/np.tan(theta) + (i+1/num_of_particles)*spread
        
     #   plt.plot([x1,x2],[y1,y2])

plt.xlim(x_origin,x_origin+canvas_size)
plt.ylim(y_origin,y_origin+canvas_size)

plt.show()
