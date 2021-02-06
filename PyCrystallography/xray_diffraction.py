from PyCrystallography.lattice import make_lattice_2d
from PyCrystallography.unit_cell import primitive_cell_2d

import numpy as np
import matplotlib
try:
    matplotlib.use('TkAgg')
except:
    pass
    
import matplotlib.pyplot as plt

# fig params
# orgin (bottom left)
x_origin = 0
y_origin = -10
canvas_size = 16

# make lattice
plt.figure('Xray-Diffraction',figsize=(5,5))
primitive_cell_2d = primitive_cell_2d('square')
lattice_points = make_lattice_2d(primitive_cell_2d,depth=canvas_size)


#print(lattice_points)

# fire particles

# angle fro surface norm (degrees)
theta = 45

#cant be zero min = 1
num_of_particles = 3
#cant be zero min = 1
# x distance incomving particles are distribued across
spread = 3


#print experiment summary init conds
print('init conds')
print(' - {} particles spread across {} in x at a angle of {} degrees\n'.format(num_of_particles,spread,theta))

#compute angles and collisions

def braggs_law(n,lambd,theta):
    """
    return lattic distancing
    """
    d = n*lambd/(2*np.sin(theta))

    return d


def check_deg(x1,x2,y1,y2):
    """
    checks a gradien matches an angle
    """
    deg = np.degrees(np.arctan((y2-y1)/(x2-x1)))
    print(deg)


def collisions(lattice_points,particle_num,theta,spread):
    """
    boolean colision indicator
    """
    for lattice_point in lattice_points:

        x = lattice_point[0]
        y = lattice_point[1]

        m = np.tan(theta)

        d_x = (particle_num/num_of_particles)*spread
        c = y_origin
        #print(c)

        
        # calcualte x and y of particle traj given lattic coords
        y_calc = m*(x + d_x) +c
        x_calc = (y -c)/m + d_x
       # print(x,x_calc)


        #print (c)

        #detection sensitivity
        ds = 0.9

        if (x -ds < x_calc < x + ds) and (y - ds < y_calc< y + ds):
            print('collision at ',x,x_calc,y,y_calc)
            return x_calc, y_calc

    return None,None

# reflect paricles
#plt.plot()
#collisions(lattice_points,num_of_particles,theta,spread)

theta = np.radians(theta)

num_of_collisions = 0

for i in range(0,num_of_particles):

    x1 = x_origin + (i/num_of_particles)*spread
    y1 =y_origin

    x2c,y2c = collisions(lattice_points,i,theta,spread) 
    if x2c != None:

        x2,y2 = x2c,y2c
        
        num_of_collisions += 1

        # d_x = (i/num_of_particles)*spread
        # c = d_x*np.tan(theta)  

        # x2 = (y2 )/np.tan(theta) + d_x
        # # plot reflected particle
        x3 = x_origin + canvas_size
        m = (y2-y1)/(x2-x1)

        #need to fgure out c
        c = 0
        y3 = -m*x3 + c
        plt.plot([x1,x2,x3],[y1,y2,y3]) 
        
    else:
        #working dont change
        # if no collision plot til canvas edge
        y2 = y_origin + canvas_size
        c = y_origin
        m = np.tan(theta)

        x2 = (y2-c)/m + (i/num_of_particles)*spread
        plt.plot([x1,x2],[y1,y2])

plt.xlim(x_origin-0.5,x_origin+canvas_size-0.5)
plt.ylim(y_origin-0.5,y_origin+canvas_size-0.5)

print('final summary')
print(' - {} lattice collision/s, {} lattice pass/es'.format(num_of_collisions,num_of_particles -num_of_collisions))
plt.tight_layout()
plt.show()
