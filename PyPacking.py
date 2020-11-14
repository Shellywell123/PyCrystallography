import matplotlib.pyplot as plt
import numpy as np

def triangle_subdivision(n):
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

    x_verts.append(x_verts[0])
    y_verts.append(y_verts[0])
    plt.plot(x_verts,y_verts,linewidth=0.5)

    # 
    x_verts = x_verts[:-1]
    y_verts = y_verts[:-1]

    def divide_tri(x_verts,y_verts):
        x_centre = np.mean(x_verts)
        y_centre = np.mean(y_verts)
     
        x_verts_new = []
        y_verts_new = []

        for x,y in zip(x_verts,y_verts):
            x_vert_new=x_centre+(x_centre-x)/2
            y_vert_new=y_centre+(y_centre-y)/2

            x_verts_new.append(x_vert_new)
            y_verts_new.append(y_vert_new)

            plt.plot([x,x_vert_new],[y,y_vert_new],linewidth=0.5)

        triangle_1 = [[x_verts[0],x_verts_new[1],x_centre],[y_verts[0],y_verts_new[1],y_centre]]
        triangle_2 = [[x_verts[0],x_verts_new[2],x_centre],[y_verts[0],y_verts_new[2],y_centre]]
        triangle_3 = [[x_verts[1],x_verts_new[0],x_centre],[y_verts[1],y_verts_new[0],y_centre]]
        triangle_4 = [[x_verts[1],x_verts_new[2],x_centre],[y_verts[1],y_verts_new[2],y_centre]]
        triangle_5 = [[x_verts[2],x_verts_new[0],x_centre],[y_verts[2],y_verts_new[0],y_centre]]
        triangle_6 = [[x_verts[2],x_verts_new[1],x_centre],[y_verts[2],y_verts_new[1],y_centre]]

        sub_triangles = [triangle_1,triangle_2,triangle_3,triangle_4,triangle_5,triangle_6]
        return sub_triangles


    # sub_triangles = divide_tri(x_verts,y_verts)
    # for triangle in sub_triangles:
    #     x_verts,y_verts = triangle[0],triangle[1]
    #     divide_tri(x_verts,y_verts)


    def n_div(x_verts,y_verts, n):
        if n >= 1:
            sub_triangles = divide_tri(x_verts,y_verts)
            for triangle in sub_triangles:
                x_verts,y_verts = triangle[0],triangle[1]
                n_div(x_verts,y_verts,n-1)
    n_div(x_verts,y_verts, n)

   # plt.show()

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
    plt.show()

#pack(5)
#triangle_subdivision(3)