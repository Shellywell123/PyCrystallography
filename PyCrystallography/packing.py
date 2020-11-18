import matplotlib.pyplot as plt
import numpy as np

def plot_triangle(triangle):
    """
    plots triangle  = (color,xpoints,ypoints)
    """
    col    = triangle[0]
    x_vals = triangle[1]
    y_vals = triangle[2]

    plt.fill(x_vals,y_vals,color=col, edgecolor='k', linewidth=0.5)

def triangle_subdivision(n,pattern_name):
    """
    makes a fractal of triangluar subdivisions
    with n deep divisions
    """

    #plot main triangle
    r=1

    d_theta = 2*np.pi/3

    x_verts = []
    y_verts = []

    for i in range(0,100):

        theta = i*2*np.pi/3 + np.pi/2

        x = r*np.cos(theta)
        y = r*np.sin(theta)
        x_verts.append(x)
        y_verts.append(y)

    start_triangle = ['red',x_verts,y_verts]

    plot_triangle(start_triangle)

    def divide_tri_diag(x_verts,y_verts):
        x_centre = np.mean(x_verts)
        y_centre = np.mean(y_verts)
     
        x_verts_new = []
        y_verts_new = []

        for x,y in zip(x_verts,y_verts):
            x_vert_new=x_centre+(x_centre-x)/2
            y_vert_new=y_centre+(y_centre-y)/2

            x_verts_new.append(x_vert_new)
            y_verts_new.append(y_vert_new)

        triangle_1 = ['green',[x_verts[0],x_verts_new[1],x_centre],[y_verts[0],y_verts_new[1],y_centre]]
        triangle_2 = ['blue',[x_verts[0],x_verts_new[2],x_centre],[y_verts[0],y_verts_new[2],y_centre]]
        triangle_3 = ['yellow',[x_verts[1],x_verts_new[0],x_centre],[y_verts[1],y_verts_new[0],y_centre]]
        triangle_4 = ['orange',[x_verts[1],x_verts_new[2],x_centre],[y_verts[1],y_verts_new[2],y_centre]]
        triangle_5 = ['purple',[x_verts[2],x_verts_new[0],x_centre],[y_verts[2],y_verts_new[0],y_centre]]
        triangle_6 = ['brown',[x_verts[2],x_verts_new[1],x_centre],[y_verts[2],y_verts_new[1],y_centre]]

        sub_triangles = [triangle_1,triangle_2,triangle_3,triangle_4,triangle_5,triangle_6]
        return sub_triangles

    def divide_tri_zelda(x_verts,y_verts):
        x_centre = np.mean(x_verts)
        y_centre = np.mean(y_verts)
     
        x_verts_new = []
        y_verts_new = []


        x_verts_new.append((x_verts[0]+x_verts[1])/2)
        y_verts_new.append((y_verts[0]+y_verts[1])/2)

        x_verts_new.append((x_verts[1]+x_verts[2])/2)
        y_verts_new.append((y_verts[1]+y_verts[2])/2)

        x_verts_new.append((x_verts[0]+x_verts[2])/2)
        y_verts_new.append((y_verts[0]+y_verts[2])/2)

        triangle_1 = ['green', [x_verts[0],x_verts_new[0],x_verts_new[2]],[y_verts[0],y_verts_new[0],y_verts_new[2]]]
        triangle_2 = ['yellow',[x_verts_new[0],x_verts[1],x_verts_new[1]],[y_verts_new[0],y_verts[1],y_verts_new[1]]]
        triangle_3 = ['blue',  [x_verts_new[1],x_verts[2],x_verts_new[2]],[y_verts_new[1],y_verts[2],y_verts_new[2]]]

        sub_triangles = [triangle_1,triangle_2,triangle_3]
        return sub_triangles

    def divide_tri_grid(x_verts,y_verts):
        x_centre = np.mean(x_verts)
        y_centre = np.mean(y_verts)
     
        x_verts_new = []
        y_verts_new = []


        x_verts_new.append((x_verts[0]+x_verts[1])/2)
        y_verts_new.append((y_verts[0]+y_verts[1])/2)

        x_verts_new.append((x_verts[1]+x_verts[2])/2)
        y_verts_new.append((y_verts[1]+y_verts[2])/2)

        x_verts_new.append((x_verts[0]+x_verts[2])/2)
        y_verts_new.append((y_verts[0]+y_verts[2])/2)

        triangle_1 = ['green', [x_verts[0],x_verts_new[0],x_verts_new[2]],[y_verts[0],y_verts_new[0],y_verts_new[2]]]
        triangle_2 = ['red',   [x_verts_new[0],x_verts_new[1],x_verts_new[2]],[y_verts_new[0],y_verts_new[1],y_verts_new[2]]]
        triangle_3 = ['yellow',[x_verts_new[0],x_verts[1],x_verts_new[1]],[y_verts_new[0],y_verts[1],y_verts_new[1]]]
        triangle_4 = ['blue',  [x_verts_new[1],x_verts[2],x_verts_new[2]],[y_verts_new[1],y_verts[2],y_verts_new[2]]]

        sub_triangles = [triangle_1,triangle_2,triangle_3,triangle_4]
        return sub_triangles

    def n_div(x_verts,y_verts, n):
        if n >= 1:
            if pattern_name == 'zelda':
                sub_triangles = divide_tri_zelda(x_verts,y_verts)
            if pattern_name == 'diag':
                sub_triangles = divide_tri_diag(x_verts,y_verts)
            if pattern_name == 'grid':
                sub_triangles = divide_tri_grid(x_verts,y_verts)
            for triangle in sub_triangles:
                plot_triangle(triangle)
                x_verts,y_verts = triangle[1],triangle[2]
                n_div(x_verts,y_verts,n-1)
    n_div(x_verts,y_verts, n)
    plt.xlim([-1,1])
    plt.ylim([-1,1])
    plt.axis('off')

def pack(num_of_sides):
    """
    """

    plt.figure()
    r = 1

    d_theta = 2*np.pi/num_of_sides

    #plot first circl
    for i in range(0,100):

        theta = i*2*np.pi/100

        x = r*np.cos(theta)
        y = r*np.sin(theta)
        plt.scatter(x,y,c='k',s=1)

    #do all ops

    d_r = 2*r*np.cos(d_theta/2)

    for j in range(0,num_of_sides):

        d_x = d_r*np.cos(j*d_theta)#+d_theta/2)
        d_y = d_r*np.sin(j*d_theta)#+d_theta/2)

        for i in range(0,100):

            theta_c = i*2*np.pi/100

            x = r*np.cos(theta_c)+d_x
            y = r*np.sin(theta_c)+d_y
            plt.scatter(x,y,c='k',s=1)

        verts_x = []
        verts_y = []
        for i in range(0,num_of_sides):

            theta = i*d_theta

            x = r*np.cos(theta+d_theta/2)+d_x
            y = r*np.sin(theta+d_theta/2)+d_y
            verts_x.append(x)
            verts_y.append(y)

            plt.scatter(x,y)
        verts_x.append(verts_x[0])
        verts_y.append(verts_y[0])
        plt.plot(verts_x,verts_y,c='k')
    plt.grid()
    plt.xlim([-1,1])
    plt.ylim([-1,1])
    plt.axis('off')

######################################################

def Penrose_Tiling(n,pattern_name):
    """
    """

    def subdivide(triangles):
        """
        """

        golden_ratio = (1+np.sqrt(5))/2

        col_1st = 'green'
        col_2nd = 'blue'

        sub_triangles = []
        for triangle in triangles:

            color = triangle[0]

            A_x = triangle[1][0]
            A_y = triangle[2][0]
            B_x = triangle[1][1]
            B_y = triangle[2][1]
            C_x = triangle[1][2]
            C_y = triangle[2][2]

            if color == col_1st:
                P_x = A_x + (B_x - A_x) / golden_ratio
                P_y = A_y + (B_y - A_y) / golden_ratio

                sub_triangle_1 = [col_1st, (C_x,P_x,B_x), (C_y,P_y,B_y)]
                sub_triangle_2 = [col_2nd, (P_x,C_x,A_x), (P_y,C_y,A_y)]

                sub_triangles.append(sub_triangle_1)
                sub_triangles.append(sub_triangle_2)

            if color == col_2nd:
                Q_x = B_x + (A_x - B_x) / golden_ratio
                Q_y = B_y + (A_y - B_y) / golden_ratio

                R_x = B_x + (C_x - B_x) / golden_ratio
                R_y = B_y + (C_y - B_y) / golden_ratio

                sub_triangle_1 = [col_2nd, (R_x,C_x,A_x), (R_y,C_y,A_y)]
                sub_triangle_2 = [col_2nd, (Q_x,R_x,B_x), (Q_y,R_y,B_y)]
                sub_triangle_3 = [col_1st, (R_x,Q_x,A_x), (R_y,Q_y,A_y)]

                sub_triangles.append(sub_triangle_1)
                sub_triangles.append(sub_triangle_2)
                sub_triangles.append(sub_triangle_3)

        return sub_triangles

    start_triangles = []

    if pattern_name == 'sun':
        for i in range(0,10):
            if i % 2 == 0:
                start_triangles.append(['green',[0,np.cos(i*np.pi/5),np.cos((i+1)*np.pi/5)],[0,np.sin(i*np.pi/5),np.sin((i+1)*np.pi/5)]])
            if i % 2 != 0:
                start_triangles.append(['green',[0,np.cos((i+1)*np.pi/5),np.cos(i*np.pi/5)],[0,np.sin((i+1)*np.pi/5),np.sin(i*np.pi/5)]])

    if pattern_name == 'star':
        rot = np.pi/10
        for i in range(0,10):
            if i % 2 == 0:
                r = 0.5/np.cos(np.pi/5)
                start_triangles.append(['blue',[r*np.cos((i+1)*np.pi/5+rot),0,np.cos(i*np.pi/5+rot),],[r*np.sin((i+1)*np.pi/5+rot),0,np.sin(i*np.pi/5+rot),]])

            if i % 2 != 0:
                r = 0.5/np.cos(np.pi/5)
                start_triangles.append(['blue',[r*np.cos(i*np.pi/5+rot),np.cos((i+1)*np.pi/5+rot),0],[r*np.sin(i*np.pi/5+rot),np.sin((i+1)*np.pi/5+rot),0]])

    for triangle in start_triangles:
        plot_triangle(triangle)
    
    def peN_div(triangles, n):
        if n >= 1:
            sub_triangles = subdivide(triangles)
            for triangle in sub_triangles:
                plot_triangle(triangle)
            peN_div(sub_triangles,n-1)

    peN_div(start_triangles, n)

    plt.xlim([-1,1])
    plt.ylim([-1,1])
    plt.axis('off')


# # #pack(5)
# triangle_subdivision(10,'zelda')
# # Penrose_Tiling(1,'star')
# # prim = primitive_cell_2d('square')
# fig = plt.figure(0,figsize=[8,8])
# ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
# from PyCrystallography import Diamond
# prim = Diamond(ax)

# fig = plt.figure(1,figsize=[8,8])
# ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
# make_lattice_3d(ax,prim)
# plt.show()