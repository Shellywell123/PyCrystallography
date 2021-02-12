

import numpy as np
import matplotlib
try:
    matplotlib.use('TkAgg')
except:
    pass
    
import matplotlib.pyplot as plt

################################################################
# functions
################################################################

def genrate_lattice_points(unit_cell_shape='square'):
    """
    generates lattice points on a figure
    """
    from PyCrystallography.lattice import make_lattice_2d
    from PyCrystallography.unit_cell import primitive_cell_2d

    primitive_cell_2d = primitive_cell_2d(unit_cell_shape)
    lattice_points = make_lattice_2d(primitive_cell_2d,depth=canvas_size)

    return lattice_points


def braggs_law(n,lambd,theta_rad):
    """
    return lattic distancing
    """
    d = n*lambd/(2*np.sin(theta_rad))

    return d


def check_deg(x1,x2,y1,y2):
    """
    checks a gradien matches an angle
    """
    deg = np.degrees(np.arctan((y2-y1)/(x2-x1)))
    print(deg)


def collision_checker(lattice_points,m,c,d_x):
    """
    trajectory lattice colision checker
    checks if a lattice point is within a range of y=mx+c
    """

    # iterate through lattic points lowest x0 -> xmax, y0->ymax
    for lattice_point in lattice_points:

        x = lattice_point[0]
        y = lattice_point[1]

        # calcualte x and y of particle traj given lattic coords
        
        x_calc = (y - c)/m + d_x
        y_calc = m*(x - d_x) + c

        #detection sensitivity (keep around 0.5 of lattice spacing)
        ds = 0.4

        #see if trajectory in range of lattice point

        d_r = np.sqrt((x-x_calc)**2+(y-y_calc)**2) 

        if d_r <= 0.4:
            return (x_calc, y_calc)

    return None


def make_wave(x_list,y_list):
    """
    """

    def z_anticlockwise(x,y,theta):
        """
        rotate around z axis
        """
        theta = -theta
        X =  x*np.cos(theta)+y*np.sin(theta)
        Y = -x*np.sin(theta)+y*np.cos(theta)

        return X,Y   

    amplitude = 0.1
    wavelength = 0.1

    #wave resolution
    N =1000

    try:
        x1,x2,x3 = x_list
        y1,y2,y3 = y_list

        theta_1 = np.arctan((y2-y1)/(x2-x1))
        theta_2 = np.arctan((y3-y2)/(x3-x2))

        length_1 = np.sqrt((y2-y1)**2+(x2-x1)**2)
        length_2 = np.sqrt((y3-y2)**2+(x3-x2)**2)

        X_1 = np.linspace(0,length_2,N)
        Y_1 = amplitude*np.sin(X_1/wavelength)

        x_1,y_1 = z_anticlockwise(X_1,Y_1,theta_1)

        x_1 = x_1 + x1
        y_1 = y_1 + y1

        X_2 = np.linspace(0,length_2,N)
        Y_2 = amplitude*np.sin(X_2/wavelength)

        x_2,y_2 = z_anticlockwise(X_2,Y_2,theta_2)

        x_2 = x_2 + x2
        y_2 = y_2 + y2

        x_ = np.concatenate((x_1,x_2))
        y_ = np.concatenate((y_1,y_2))

        plt.plot(x_,y_)

    except:
        x1,x2 = x_list
        y1,y2 = y_list

        theta = np.arctan((y2-y1)/(x2-x1))
        length_1 = np.sqrt((y2-y1)**2+(x2-x1)**2)

        x = np.linspace(0,length_1,N)
        y = amplitude*np.sin(x/wavelength)

        x_,y_ = z_anticlockwise(x,y,theta)

        x_ = x_ + x1
        y_ = y_ + y1

        plt.plot(x_,y_)


def run_simulation(num_of_particles,theta,spread,lattice_shape='square'):
    """
    runs xray diffraction simulations
    """    

    #print experiment summary init conds
    print('Initial Conditions')
    print(' - {} particles spread across {} (x units) at a angle of {} degrees\n'.format(num_of_particles,spread,theta))

    plt.figure('Xray-Diffraction',figsize=(5,5))
    plt.clf()
    lattice_points = genrate_lattice_points(unit_cell_shape=lattice_shape)

    theta_rad = np.radians(theta)

    num_of_collisions = 0

    for i in range(0,num_of_particles):

        m = np.tan(theta_rad)
        c = y_origin
        d_x = (i/num_of_particles)*spread

        x1 = x_origin + d_x
        y1 = y_origin

        collision = collision_checker(lattice_points,m,c,d_x)

        if collision:
            # if collision diffract particle trajectory
            num_of_collisions += 1

            x2,y2 = collision
            
            # set x lim to beat canvas edge
            x3 = x2+(x2-x1)
            y3 = y1

            make_wave([x1,x2,x3],[y1,y2,y3])
            
        else:
            # if no collision plot til canvas edge
            y2 = y_origin + canvas_size
            x2 = (y2-c)/m + d_x

            make_wave([x1,x2],[y1,y2])

    plt.xlim(x_origin-0.5,x_origin+canvas_size-0.5)
    plt.ylim(y_origin-0.5,y_origin+canvas_size-0.5)

    print('Simulation Outcome')
    print(' - {} lattice collision/s, {} lattice pass/es'.format(num_of_collisions,num_of_particles -num_of_collisions))
    plt.tight_layout()
    plt.show()

################################################################
# setting params
################################################################

################################
# fig params
################################
# fig params - orgin (bottom left)
x_origin = 0
y_origin = -10
canvas_size = 16

# ################################
# # simulation params
# ################################

# angle fro surface norm (degrees)
theta = 55


# number of particles being fired
# - can not be zero, min = 1
num_of_particles = 5

# x distance incomving particles are distribued across
# - can not be zero, min = 1
spread = 1

# ################################################################
# # execution
# ################################################################

# run_simulation(num_of_particles,theta,spread,lattice_shape='rhombus')