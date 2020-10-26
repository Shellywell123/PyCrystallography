import matplotlib.pyplot as plt
import numpy as np

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

pack(5)