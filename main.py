import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PyShapes import *
from PyCrystallography import *

################################################################################

def make_gif():
    """
    generates screenshots of the program across a 28 days and then compiles them into a gif
    """
    # every day date in a 28 cycle in 1 day incriments
    num_of_frames = 36
    for frame in range(0,num_of_frames+1):

        fig = plt.figure(0,figsize=[8,8])
        azim = (360/num_of_frames)*frame
        ax = fig.add_subplot(111,projection='3d',azim=azim,elev=30)

        #inversion
        #inversion(ax,7,7,7)

        #reflection  
        #reflection(ax,7,7,7)

        #rotation
        # rotation(ax,7,7,7)

        #cube
        # cuboid(ax,5,5,5)

        # cuboid
        # cuboid(ax,5,5,10)

        # #coboid1
        # cuboid(ax,5,10,5)

        # #cuboid2
        # cuboid(ax,10,5,5)

        #cube_reflection
        #cube_reflection(ax,7,7,7)

        #pramid
      #  pryamid(ax,7,10)

        #spintop
        #spintop(ax,7,10)

        # #NaCl
        # NaCl(ax)

        #fcc
       # FCC(ax)

        #bcc
        #BCC(ax)

        #tetrakis
        #tetrakis(ax,3,1)

        #diamons
        #Diamond(ax)

        #test
        test_sphere(ax)

        if frame <= 8:
            frame = '0'+str(frame+1)
        else:
            frame = str(frame+1)

        filename = 'Images/frames/{}_{}.png'.format(frame,num_of_frames)
        plt.savefig(filename)
        print(' - Image saved')

    # convert all saved images to a single gif
    import imageio
    images = []
    for filename in os.listdir('Images/frames/'):
        images.append(imageio.imread('Images/frames/'+filename))
    imageio.mimsave('Images/face_normals_cube.gif', images)
    print('gif made')

################################################################################



fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d')
Stereographic_projection(ax)

#make_gif()