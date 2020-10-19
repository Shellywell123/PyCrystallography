import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PyShapes import *

def make_gif():
    """
    generates screenshots of the program across a 28 days and then compiles them into a gif
    """
    # every day date in a 28 cycle in 1 day incriments
    num_of_frames = 36
    for frame in range(1,num_of_frames):
        fig = plt.figure(0,figsize=[8,8])
        azim = (360/num_of_frames)*frame
        ax = fig.add_subplot(111,projection='3d',azim=azim,elev=30)
        plot_axis(ax)
        cuboid(ax,5,10,5)
        
        filename = 'Images/frames/{}_{}.png'.format(frame,num_of_frames)
        plt.savefig(filename)
        print(' - Image saved')

    # convert all saved images to a single gif
    import imageio
    images = []
    for filename in os.listdir('Images/frames/'):
        images.append(imageio.imread('Images/frames/'+filename))
    imageio.mimsave('Images/cuboid2.gif', images)
    print('gif made')

################################################################################

def plot_axis(ax):
    """
    """
    ax.set_facecolor('white')
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

    ax.grid(False)

    max_lim = 10
    min_lim = -max_lim
    ax.auto_scale_xyz([min_lim, max_lim],
                [min_lim, max_lim], 
                [0, 2*max_lim])   

    #make axes at orgin
    #plt.axes(False)
    empty_list = [0,0]
    lim_list   = [min_lim,max_lim]
    pos = 0.1*max_lim
    #x axis
 #   ax.quiver(max_lim-pos,0,0,1,0,0, length=pos, normalize=True,linewidth=1)
    ax.plot(lim_list,empty_list,empty_list,linewidth=1,c='r')
    ax.text(max_lim+pos,0,0,r"$x$",c='r')
    #y axi
    #ax.quiver(0,min_lim,0,0,1,0, length=max_lim*2, normalize=True,linewidth=1)
    ax.text(0,max_lim+pos,0,r"$y$",c='green')
    ax.plot(empty_list,lim_list,empty_list,linewidth=1,c='green')
    #z axis
    #ax.quiver(0,0,min_lim,0,0,1, length=max_lim*2, normalize=True,linewidth=1)
    ax.text(0,0,max_lim+pos,r"$z$",c='blue')
    ax.plot(empty_list,empty_list,lim_list,linewidth=1,c='blue')
    ax.axis('off')


# fig = plt.figure(0,figsize=[8,8])
# ax = fig.add_subplot(111,projection='3d')
# plot_axis(ax)
# cube(ax,7,7,7)
# plt.show()
make_gif()