import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PyShapes import *
from PyCrystallography import *

################################################################################

def make_all_gifs():
    """
    generates screenshots of the program and then compiles them into a gif
    """

    objects = [{'function': 'FCC(ax)',
                'name'    : 'FCC'},

                {'function': 'BCC(ax)',
                 'name'    : 'BCC'},

                {'function': 'NaCl(ax)',
                 'name'    : 'NaCl'},

                {'function': 'Diamond(ax)',
                'name'     : 'diamond'},

                {'function': 'cuboid(ax,5,5,5)',
                 'name'    : 'cube'},

                {'function': 'cuboid(ax,10,5,5)',
                 'name'    : 'cuboid_x'},

                {'function': 'cuboid(ax,5,10,5)',
                 'name'    : 'cuboid_y'},

                {'function': 'cuboid(ax,5,5,10)',
                 'name'    : 'cuboid_z'},

                {'function': 'rotation(ax)',
                 'name'    : 'rotation'},

                {'function': 'inversion(ax)',
                 'name'    : 'inversion'},

                {'function': 'reflection(ax)',
                 'name'    : 'reflection'},

                {'function': 'cube_reflection(ax,7,7,7)',
                 'name'    : 'cube_reflection'},

                {'function': 'pyramid(ax,7,3)',
                 'name'    : 'pyramid3'},

                {'function': 'pyramid(ax,7,4)',
                 'name'    : 'pyramid4'},

                {'function': 'pyramid(ax,7,5)',
                 'name'    : 'pyramid5'},

                {'function': 'pyramid(ax,7,10)',
                 'name'    : 'pyramid10'},

                {'function': 'bipyramid(ax,7,3)',
                 'name'    : 'bipyramid3'},

                {'function': 'bipyramid(ax,7,4)',
                 'name'    : 'bipyramid4'},

                {'function': 'bipyramid(ax,7,5)',
                 'name'    : 'bipyramid5'},

                {'function': 'bipyramid(ax,7,10)',
                 'name'    : 'bipyramid10'},

                {'function': 'biprismid(ax,2,1,3)',
                 'name'    : 'biprismid3'},

                {'function': 'biprismid(ax,2,1,4)',
                 'name'    : 'biprismid4'},

                {'function': 'biprismid(ax,2,1,5)',
                 'name'    : 'biprismid5'},

                {'function': 'biprismid(ax,2,1,10)',
                 'name'    : 'biprismid10'},

                {'function': 'prism(ax,7,3)',
                 'name'    : 'prism3'},

                {'function': 'prism(ax,7,4)',
                 'name'    : 'prism4'},

                {'function': 'prism(ax,7,5)',
                 'name'    : 'prism5'},

                {'function': 'prism(ax,7,10)',
                 'name'    : 'prism10'},

                {'function': 'tetrakis(ax,3,1)',
                 'name'    : 'tetrakis'},

                {'function': 'normal_points(ax,cuboid(ax,2,2,2),2)',
                 'name'    : 'face_normals_cube'}
                ]

    for object in objects:
        num_of_frames = 36
        for frame in range(0,num_of_frames):

            fig = plt.figure(0,figsize=[8,8])
            azim = (360/num_of_frames)*frame
            ax = fig.add_subplot(111,projection='3d',azim=azim,elev=30)


            ###################################################

            function = object['function']
            eval(function)
            name = object['name']

            ####################################################

            if frame <= 8:
                frame = '0'+str(frame+1)
            else:
                frame = str(frame+1)

            filename = 'Images/frames/{}_{}.png'.format(frame,num_of_frames)
            plt.savefig(filename)
            print('Frame ({}/{}) Saved.'.format(frame,num_of_frames))

        # convert all saved images to a single gif
        import imageio
        images = []
        for filename in os.listdir('Images/frames/'):
            images.append(imageio.imread('Images/frames/'+filename))
        imageio.mimsave('Images/{}.gif'.format(name), images)
        print('{}.gif made'.format(name))

################################################################################

make_all_gifs()

fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d')
h,w,d = 2,2,5
faces = cuboid(ax,2,2,2)
r = max(h,w,d)
points=normal_points(ax,faces,r)
Stereographic_projection(ax,points,r)
plt.show()