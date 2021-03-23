import matplotlib
try:
    matplotlib.use('TkAgg')
except:
    pass

import numpy as np
import matplotlib.pyplot as plt

#####################################
# lattices
#####################################

def make_vectors_reciprocal(vectors):
    """
    TODO
    converts a list of primitve vector into their corresponing reciprcal versions
    vectors = list of vectors to convert (in order ax,ay,bx,by etc)
    """    

    #90 deg rotation matrix 
    rot_theta = np.radians(90)
    Q = [[np.cos(rot_theta), -np.sin(rot_theta)],
         [np.sin(rot_theta),  np.cos(rot_theta)]]
    # if 3 vectors (x&y) len = 6 
    print(vectors)

    if len (vectors) == 3:
        A = vectors[0]
        B = vectors[1]
        C = vectors[2]

        V = np.dot(A,np.cross(B,C))

        A_r = 2*np.pi*np.cross(B,C)/V
        B_r = 2*np.pi*np.cross(C,A)/V
        C_r = 2*np.pi*np.cross(A,B)/V
        

        print('\nunit cell volume =',V)

        print('\nreciporocal primitive vectors')
        print('A_r = ',A_r)
        print('B_r = ',B_r)
        print('C_r = ',C_r)

        vectors = [A_r,B_r,C_r]
        return vectors

    #if 2 vectors (x&y) len = 4

    if len(vectors) == 2:
     
        M=np.array([[0.,1.],[1.,0.]]) # antisymetric matrix
        n2=np.linalg.norm(ab[:,0])*np.linalg.norm(ab[:,1])# product of norms  ||a|| x ||b||
        abR=(np.dot(M,ab))/n2

def make_lattice_2d(primitive_cell_2d,depth=5):
    """
    """
    #triangle
    if len(primitive_cell_2d[0]) == 3:
        x_points,y_points = primitive_cell_2d

        r = max(max(x_points)-min(x_points),max(y_points)-min(y_points))/2

        vector_A_x = r*np.cos(2*np.pi/3)
        vector_A_y = r*np.sin(2*np.pi/3)

        vector_B_x = -r*np.cos(2*np.pi/3)
        vector_B_y = r*np.sin(2*np.pi/3)

        vector_C_x = - vector_A_x + vector_B_x
        vector_C_y = - vector_A_y + vector_B_y

        plt.plot((0,vector_A_x),(0,vector_A_y),label='A',c='b')
        plt.plot((0,vector_B_x),(0,vector_B_y),label='B',c='r')   
        plt.plot((0,vector_C_x),(0,vector_C_y),label='C',c='g')   
        plt.scatter(0,0,c='k')

        lattice_points = []

        for i in range(0,depth):
            for j in range(0,depth):

                if (j%2 == 0):
                    # draws \ shape repeated over a grid
                    # bottom left (main base origin)
                    x_lattice_point_1 = vector_C_x*i 
                    y_lattice_point_1 = vector_C_y*j + (vector_A_y)*j
                    plt.scatter(x_lattice_point_1,y_lattice_point_1, c='k')
                    lattice_points.append([x_lattice_point_1,y_lattice_point_1])

                    # top left
                    x_lattice_point_2 = x_lattice_point_1 + vector_A_x
                    y_lattice_point_2 = y_lattice_point_1 + vector_A_y
                    plt.scatter(x_lattice_point_2,y_lattice_point_2, c='k')
                    lattice_points.append([x_lattice_point_2,y_lattice_point_2])

                    #lattice bonds
                    alph = 0.2
                    lc = 'k'
                    plt.plot((x_lattice_point_1,x_lattice_point_1+vector_A_x),(y_lattice_point_1,y_lattice_point_1+vector_A_y),alpha=alph,c=lc)
                    plt.plot((x_lattice_point_1,x_lattice_point_1+vector_B_x),(y_lattice_point_1,y_lattice_point_1+vector_B_y),alpha=alph,c=lc)   
                    plt.plot((x_lattice_point_1,x_lattice_point_1+vector_C_x),(y_lattice_point_1,y_lattice_point_1+vector_C_y),alpha=alph,c=lc)   
                    
                    plt.plot((x_lattice_point_1+vector_A_x,x_lattice_point_1+2*vector_A_x),(y_lattice_point_1+vector_A_y,y_lattice_point_1+2*vector_A_y),alpha=alph,c=lc)
                    plt.plot((x_lattice_point_1+vector_B_x,x_lattice_point_1+2*vector_B_x),(y_lattice_point_1+vector_B_y,y_lattice_point_1+2*vector_B_y),alpha=alph,c=lc)   
                    plt.plot((x_lattice_point_1+vector_B_x,x_lattice_point_1+vector_B_x-vector_C_x),(y_lattice_point_1+vector_B_y,y_lattice_point_1+vector_B_y-vector_C_y),alpha=alph,c=lc)   
                    

    #for hexagonal and more complex lattices need new algo
    if len(primitive_cell_2d[0]) == 6:
        x_points,y_points = primitive_cell_2d

        r = max(max(x_points)-min(x_points),max(y_points)-min(y_points))/2

        vector_A_x = 0
        vector_A_y = r

        vector_B_x = r*np.cos(np.pi/6)
        vector_B_y = -r*np.sin(np.pi/6)

        vector_C_x = -r*np.cos(np.pi/6)
        vector_C_y = -r*np.sin(np.pi/6) 

        plt.plot((0,vector_A_x),(0,vector_A_y),label='A',c='b')
        plt.plot((0,vector_B_x),(0,vector_B_y),label='B',c='r')   
        plt.plot((0,vector_C_x),(0,vector_C_y),label='C',c='g')   
        plt.scatter(0,0,c='k')

        lattice_points =[]

        for i in range(0,depth):
            for j in range(0,depth):

                if (j%2 == 0):
                    # draws backwards C shape repeated over a grid
                    # bottom mid (main base origin)
                    x_lattice_point_1 = (vector_B_x - vector_C_x)*i 
                    y_lattice_point_1 = (vector_B_y - vector_C_y)*j + (vector_A_y-vector_B_y)*j
                    plt.scatter(x_lattice_point_1,y_lattice_point_1, c='k')
                    lattice_points.append([x_lattice_point_1,y_lattice_point_1])

                    # top mid 
                    x_lattice_point_2 = x_lattice_point_1 + vector_A_x
                    y_lattice_point_2 = y_lattice_point_1 + vector_A_y
                    plt.scatter(x_lattice_point_2,y_lattice_point_2, c='k')
                    lattice_points.append([x_lattice_point_2,y_lattice_point_2])

                    #bottom left
                    x_lattice_point_3 = x_lattice_point_1 + vector_C_x
                    y_lattice_point_3 = y_lattice_point_1 + vector_C_y
                    plt.scatter(x_lattice_point_3,y_lattice_point_3, c='k')
                    lattice_points.append([x_lattice_point_3,y_lattice_point_3])

                    #top left
                    x_lattice_point_4 = x_lattice_point_2 - vector_B_x
                    y_lattice_point_4 = y_lattice_point_2 - vector_B_y
                    plt.scatter(x_lattice_point_4,y_lattice_point_4, c='k')
                    lattice_points.append([x_lattice_point_4,y_lattice_point_4])

                    #need to draw hex lattic lines still
                    alph = 0.2
                    lc = 'k'
                    plt.plot((x_lattice_point_1,x_lattice_point_1+vector_A_x),(y_lattice_point_1,y_lattice_point_1+vector_A_y),alpha=alph,c=lc)
                    plt.plot((x_lattice_point_1,x_lattice_point_1+vector_B_x),(y_lattice_point_1,y_lattice_point_1+vector_B_y),alpha=alph,c=lc)
                    plt.plot((x_lattice_point_1,x_lattice_point_1+vector_C_x),(y_lattice_point_1,y_lattice_point_1+vector_C_y),alpha=alph,c=lc)
                    plt.plot((x_lattice_point_2,x_lattice_point_2-vector_C_x),(y_lattice_point_2,y_lattice_point_2-vector_C_y),alpha=alph,c=lc)
                    plt.plot((x_lattice_point_2,x_lattice_point_2-vector_B_x),(y_lattice_point_2,y_lattice_point_2-vector_B_y),alpha=alph,c=lc)
                    plt.plot((x_lattice_point_2-vector_B_x,x_lattice_point_2-vector_B_x+vector_A_x),(y_lattice_point_2-vector_B_y,y_lattice_point_2-vector_B_y+vector_A_y),alpha=alph,c=lc)
                    

    #for square and rhobic lattices
    if len(primitive_cell_2d[0]) == 4:
        x_points,y_points = primitive_cell_2d

        vector_A_x = abs(x_points[1] - x_points[0])
        vector_A_y = abs(y_points[1] - y_points[0])

        vector_B_x = abs(x_points[2] - x_points[0])
        vector_B_y = abs(y_points[2] - y_points[0])    

        plt.plot((0,vector_A_x),(0,vector_A_y),label='A',c='b')
        plt.plot((0,vector_B_x),(0,vector_B_y),label='B',c='r')

        A = [[0,vector_A_x],
             [0,vector_A_y]]

        B = [[0,vector_B_x],
             [0,vector_B_y]]
        
        #C = [[0,vector_C_x],
        #     [0,vector_C_y]]

        vectors = [A,B]
        make_vectors_reciprocal(vectors)

        lattice_points = []

        for i in range(0,depth):
            for j in range(0,depth):
                x_lattice_point_1 = (vector_A_x*i+vector_B_x*j)
                y_lattice_point_1 = (vector_A_y*i+vector_B_y*j)
                plt.scatter(x_lattice_point_1,y_lattice_point_1,c='k')
                lattice_points.append([x_lattice_point_1,y_lattice_point_1])

                #lattice bonds
                alph = 0.2
                lc = 'k'
                plt.plot((x_lattice_point_1,x_lattice_point_1+vector_A_x),(y_lattice_point_1,y_lattice_point_1+vector_A_y),alpha=alph,c=lc)
                plt.plot((x_lattice_point_1,x_lattice_point_1+vector_B_x),(y_lattice_point_1,y_lattice_point_1+vector_B_y),alpha=alph,c=lc)

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

    tag =''

    ax.plot(
        (min(x_points),min(x_points)+vector_A_x),
        (min(y_points),min(y_points)+vector_A_y),
        (min(z_points),min(z_points)+vector_A_z), 
        label='A'+tag,c='b')

    ax.plot(
        (min(x_points),min(x_points)+vector_B_x),
        (min(y_points),min(y_points)+vector_B_y),
        (min(z_points),min(z_points)+vector_B_z),
        label='B'+tag,c='r')

    ax.plot(
        (min(x_points),min(x_points)+vector_C_x),
        (min(y_points),min(y_points)+vector_C_y),
        (min(z_points),min(z_points)+vector_C_z),
        label='C'+tag,c='g')

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

def make_lattice_3d_reciprocal(ax,primitive_cell_3d,depth=2):
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
    vector_A_x_ = abs(max(x_points) - min(x_points))
    vector_A_y_ = 0
    vector_A_z_ = 0

    vector_B_x_ = 0
    vector_B_y_ = abs(max(y_points) - min(y_points))  
    vector_B_z_ = 0 

    vector_C_x_ = 0
    vector_C_y_ = 0    
    vector_C_z_ = abs(max(z_points) - min(z_points))

    #print(vector_A_x,vector_B_x,vector_C_x)
    # considering making all unit cells be saved as unit vectors
    tag ='_r'
    #pack vectrs
    A = [vector_A_x_,
        vector_A_y_,
        vector_A_z_]

    B = [vector_B_x_,
        vector_B_y_,
        vector_B_z_]

    C = [vector_C_x_,
        vector_C_y_,
        vector_C_z_]

    print('\nprimitive vectors')
    print('A = ',A)
    print('B = ',B)
    print('C = ',C)

    vectors = [A,B,C]
    vectors_r=make_vectors_reciprocal(vectors)

    # unpack recipvects
    A_r,B_r,C_r = vectors_r

    vector_A_x,vector_A_y,vector_A_z = A
    vector_B_x,vector_B_y,vector_B_z = B
    vector_C_x,vector_C_y,vector_C_z = C

    # ax.plot(
    #     (-1,1+vector_A_x),
    #     (-1,1+vector_A_y),
    #     (-1,1+vector_A_z), 
    #     label='A'+tag,c='b')

    # ax.plot(
    #     (-1,1+vector_B_x),
    #     (-1,1+vector_B_y),
    #     (-1,1+vector_B_z),
    #     label='B'+tag,c='r')

    # ax.plot(
    #     (-1,1+vector_C_x),
    #     (-1,1+vector_C_y),
    #     (-1,1+vector_C_z),
    #     label='C'+tag,c='g')

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
                        c=k,
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