import matplotlib.pyplot as plt
import numpy as np

def degrees_to_radians(angle):
    """
    degrees to radians angle converter
    """
    angle = float(angle/180)*np.pi
    return angle


def rotate_coords(x,y,theta):
    """
    """
    theta = degrees_to_radians(theta)

    X =  x*np.cos(theta)+y*np.sin(theta)
    Y = -x*np.sin(theta)+y*np.cos(theta)

    return X,Y


def linear_rot_pattern(rot):
    """
    """
    fig = plt.figure(figsize=[8,8])
    ax = fig.add_subplot(111)

    h = 150
    for i in range(int(-h/2),int(h/2)):
        x1=x2=i
        y1=-h/2
        y2=h/2
        ax.plot([x1,x2],[y1,y2],c='k')

        x1_rot,y1_rot = rotate_coords(x1,y1,rot)
        x2_rot,y2_rot = rotate_coords(x2,y2,rot)
        ax.plot([x1_rot,x2_rot],[y1_rot,y2_rot],c='k')

    ax.axis('off')
    ax.set_xlim([-h/3,h/3])
    ax.set_ylim([-h/3,h/32])
    #plt.show()

def radial_seperation_pattern(sep):
    """
    """
    fig = plt.figure(figsize=[8,8])
    ax = fig.add_subplot(111)


    h = 150
    for r in range(0,h):
        
        x_points = []
        y_points = []

        theta = np.linspace(0,2*np.pi,100)

        x = r*np.cos(theta) - sep/2
        y = r*np.sin(theta)

        ax.plot(x,y,c='k')

        x_sep = x + sep
        y_sep = y 

        ax.plot(x_sep,y_sep,c='k')

    ax.axis('off')
    ax.set_xlim([-h/3,h/3])
    ax.set_ylim([-h/3,h/3])
    #plt.show()