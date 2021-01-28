import matplotlib
try:
    matplotlib.use('TkAgg')
except:
    pass
    
import matplotlib.pyplot as plt

#####################################
# lattices
#####################################


def make_lattice_2d(primitive_cell_2d,depth=5):
    """
    """

    x_points,y_points = primitive_cell_2d

    vector_A_x = abs(x_points[1] - x_points[0])
    vector_A_y = abs(y_points[1] - y_points[0])

    vector_B_x = abs(x_points[2] - x_points[0])
    vector_B_y = abs(y_points[2] - y_points[0])    

    plt.plot((0,vector_A_x),(0,vector_A_y),label='A',c='b')
    plt.plot((0,vector_B_x),(0,vector_B_y),label='B',c='r')

    lattice_points = []

    for i in range(0,depth):
        for j in range(0,depth):
            plt.scatter((vector_A_x*i+vector_B_x*j),(vector_A_y*i+vector_B_y*j),c='k')
            lattice_points.append([(vector_A_x*i+vector_B_x*j),(vector_A_y*i+vector_B_y*j)])

    plt.legend(loc='upper left')
    plt.axis('off')
    return lattice_points

def make_lattice_3d(ax,primitive_cell_3d,depth=2):
    """
    """

    atoms,bonds = primitive_cell_3d

    x_points = []
    y_points = []
    z_points = []

    for atom in atoms:
        x   = atom['x']
        y   = atom['y']
        z   = atom['z']

        x_points.append(x[0])
        y_points.append(y[0])
        z_points.append(z[0])

        col = atom['color']
        siz = atom['size']

    # maybe get vectors from bonds 
    vector_A_x = abs(max(x_points) - min(x_points))
    vector_A_y = 0
    vector_A_z = 0

    vector_B_x = 0
    vector_B_y = abs(max(y_points) - min(y_points))  
    vector_B_z = 0 

    vector_C_x = 0
    vector_C_y = 0    
    vector_C_z = abs(max(z_points) - min(z_points))

    #print(vector_A_x,vector_B_x,vector_C_x)

    ax.plot(
        (min(x_points),min(x_points)+vector_A_x),
        (min(y_points),min(y_points)+vector_A_y),
        (min(z_points),min(z_points)+vector_A_z), 
        label='A',c='b')

    ax.plot(
        (min(x_points),min(x_points)+vector_B_x),
        (min(y_points),min(y_points)+vector_B_y),
        (min(z_points),min(z_points)+vector_B_z),
        label='B',c='r')

    ax.plot(
        (min(x_points),min(x_points)+vector_C_x),
        (min(y_points),min(y_points)+vector_C_y),
        (min(z_points),min(z_points)+vector_C_z),
        label='C',c='g')

    for atom in atoms:
        x   = atom['x'][0]
        y   = atom['y'][0]
        z   = atom['z'][0]
        col = atom['color']
        siz = atom['size']/(depth+1) #so that you get persp on gif
        for i in range(0,depth):
            for j in range(0,depth):
                for k in range(0,depth):
                    ax.scatter(
                        x+(vector_A_x*i+vector_B_x*j+vector_C_x*k),
                        y+(vector_A_y*i+vector_B_y*j+vector_C_y*k),
                        z+(vector_A_z*i+vector_B_z*j+vector_C_z*k),
                        c=col,
                        s=siz)

    for bond in bonds:
        x1,x2 = bond['x']
        y1,y2 = bond['y']
        z1,z2 = bond['z']
        col   = bond['color']
        siz   = bond['size']/(depth+1) #so that you get persp on gif
        for i in range(0,depth):
            for j in range(0,depth):
                for k in range(0,depth):

                    x_plot = [x1+(vector_A_x*i+vector_B_x*j+vector_C_x*k),
                              x2+(vector_A_x*i+vector_B_x*j+vector_C_x*k)]
                    y_plot = [y1+(vector_A_y*i+vector_B_y*j+vector_C_y*k),
                              y2+(vector_A_y*i+vector_B_y*j+vector_C_y*k)]
                    z_plot = [z1+(vector_A_z*i+vector_B_z*j+vector_C_z*k),
                              z2+(vector_A_z*i+vector_B_z*j+vector_C_z*k)]
                    ax.plot(x_plot,y_plot,z_plot,c=col,linewidth=siz)

    ax.legend()
    ax.axis('off')