

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

        # fix y_calc!!!!!!!!
        y_calc = m*(x - d_x) + c

        #detection sensitivity (keep around 0.5 of lattice spacing)
        ds = 0.2

        #see if trajectory in range of lattice point
        # replace with radial checker soon
       # if (x -ds < x_calc < x + ds) and (y - ds < y_calc< y + ds):
           # print('collision at ',x,x_calc,y,y_calc)
        #    return (x_calc, y_calc)

        d_r = np.sqrt((x-x_calc)**2+(y-y_calc)**2) 

        if d_r <= 0.4:
            return (x_calc, y_calc)

    return None


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

            plt.plot([x1,x2,x3],[y1,y2,y3]) 
            
        else:
            # if no collision plot til canvas edge
            y2 = y_origin + canvas_size
            x2 = (y2-c)/m + d_x

            plt.plot([x1,x2],[y1,y2])

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

# # angle fro surface norm (degrees)
# theta = 60


# # number of particles being fired
# # - can not be zero, min = 1
# num_of_particles = 3

# # x distance incomving particles are distribued across
# # - can not be zero, min = 1
# spread = 1

# ################################################################
# # execution
# ################################################################

# run_simulation(num_of_particles,theta,spread,lattice_shape='square')