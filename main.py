import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PyShapes import *
from PyCrystallography import *

################################################################################

def make_all_structure_gifs():
    """
    generates screenshots of the program and then compiles them into a gif
    """

    objects = [
                {'code'     : 'FCC(ax)',
                 'name'     : 'FCC'},

                {'code'     : 'BCC(ax)',
                 'name'     : 'BCC'},

                {'code'     : 'NaCl(ax)',
                 'name'     : 'NaCl'},

                {'code'     : 'Diamond(ax)',
                 'name'     : 'diamond'}

                ]

    for object in objects:
        num_of_frames = 36
        for frame in range(0,num_of_frames):

            fig = plt.figure(0,figsize=[8,8])
            azim = (360/num_of_frames)*frame
            ax = fig.add_subplot(111,projection='3d',azim=azim,elev=30)

            ###################################################

            code = object['code']
            exec(code)
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

def make_all_operations_gifs():
    """
    generates screenshots of the program and then compiles them into a gif
    """

    objects = [
                {'code'    : 'rotation(ax,2,2,2)',
                 'name'    : 'rotation'},

                {'code'    : 'inversion(ax,2,2,2)',
                 'name'    : 'inversion'},

                {'code'    : 'reflection(ax,2,2,2)',
                 'name'    : 'reflection'}
                ]

    for object in objects:
        num_of_frames = 36
        for frame in range(0,num_of_frames):

            fig = plt.figure(0,figsize=[8,8])
            azim = (360/num_of_frames)*frame
            ax = fig.add_subplot(111,projection='3d',azim=azim,elev=30)

            ###################################################

            code = object['code']
            exec(code)
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

def make_all_face_norm_gifs():
    """
    generates screenshots of the program and then compiles them into a gif
    """

    objects = [

                {'code'    : 'points = normal_points(ax,cuboid(ax,2,2,2),2)',
                 'name'    : 'face_normals_cube'},

                {'code'    : 'normal_points(ax,pyramid(ax,1,0.5,3),1)',
                 'name'    : 'face_normals_pyramid'},

                {'code'    : 'normal_points(ax,bipyramid(ax,1,0.5,6),1)',
                 'name'    : 'face_normals_bipyramid'},

                {'code'    : 'normal_points(ax,prism(ax,2,2,6),2)',
                 'name'    : 'face_normals_prism'},

                {'code'    : 'normal_points(ax,biprismid(ax,3,1,0.5,5),1)',
                 'name'    : 'face_normals_biprismid'}
                         ]

    for object in objects:
        num_of_frames = 36
        for frame in range(0,num_of_frames):

            fig = plt.figure(0,figsize=[8,8])
            azim = (360/num_of_frames)*frame
            ax = fig.add_subplot(111,projection='3d',azim=azim,elev=30)

            ###################################################

            code = object['code']
            exec(code)
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

def make_all_shape_gifs():
    """
    generates screenshots of the program and then compiles them into a gif
    """

    objects = [
                {'code'    : 'cuboid(ax,5,5,5)',
                 'name'    : 'cube'},

                {'code'    : 'cuboid(ax,10,5,5)',
                 'name'    : 'cuboid_x'},

                {'code'    : 'cuboid(ax,5,10,5)',
                 'name'    : 'cuboid_y'},

                {'code'    : 'cuboid(ax,5,5,10)',
                 'name'    : 'cuboid_z'},

                {'code'    : 'pyramid(ax,1,0.5,3)',
                 'name'    : 'pyramid3'},

                {'code'    : 'pyramid(ax,1,0.5,4)',
                 'name'    : 'pyramid4'},

                {'code'    : 'pyramid(ax,1,0.5,5)',
                 'name'    : 'pyramid5'},

                {'code'    : 'pyramid(ax,1,0.5,10)',
                 'name'    : 'pyramid10'},

                {'code'    : 'bipyramid(ax,1,0.5,3)',
                 'name'    : 'bipyramid3'},

                {'code'    : 'bipyramid(ax,1,0.5,4)',
                 'name'    : 'bipyramid4'},

                {'code'    : 'bipyramid(ax,1,0.5,5)',
                 'name'    : 'bipyramid5'},

                {'code'    : 'bipyramid(ax,1,0.5,10)',
                 'name'    : 'bipyramid10'},

                {'code'    : 'biprismid(ax,3,1,0.5,3)',
                 'name'    : 'biprismid3'},

                {'code'    : 'biprismid(ax,3,1,0.5,4)',
                 'name'    : 'biprismid4'},

                {'code'    : 'biprismid(ax,3,1,0.5,5)',
                 'name'    : 'biprismid5'},

                {'code'    : 'biprismid(ax,3,1,0.5,10)',
                 'name'    : 'biprismid10'},

                {'code'    : 'prism(ax,2,2,3)',
                 'name'    : 'prism3'},

                {'code'    : 'prism(ax,2,2,4)',
                 'name'    : 'prism4'},

                {'code'    : 'prism(ax,2,2,5)',
                 'name'    : 'prism5'},

                {'code'    : 'prism(ax,2,2,10)',
                 'name'    : 'prism10'},

                {'code'    : 'tetrakis(ax,3,1)',
                 'name'    : 'tetrakis'},

                {'code'    : 'points = normal_points(ax,cuboid(ax,2,2,2),2)',
                 'name'    : 'face_normals_cube'},

                {'code'    : 'normal_points(ax,pyramid(ax,1,0.5,3),1)',
                 'name'    : 'face_normals_pyramid'},

                {'code'    : 'normal_points(ax,bipyramid(ax,1,0.5,6),1)',
                 'name'    : 'face_normals_bipyramid'},

                {'code'    : 'normal_points(ax,prism(ax,2,2,6),2)',
                 'name'    : 'face_normals_prism'},

                {'code'    : 'normal_points(ax,biprismid(ax,3,1,0.5,5),1)',
                 'name'    : 'face_normals_biprismid'}
                         ]

    for object in objects:
        num_of_frames = 36
        for frame in range(0,num_of_frames):

            fig = plt.figure(0,figsize=[8,8])
            azim = (360/num_of_frames)*frame
            ax = fig.add_subplot(111,projection='3d',azim=azim,elev=30)

            ###################################################

            code = object['code']
            exec(code)
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

def make_all_stereos():
    """
    """
    stereos = [
                {'code': """points = normal_points(ax,cuboid(ax,2,2,2),2);Stereographic_projection(ax,points,2,'stereographic_projection_cube')"""},
       
                {'code': """points = normal_points(ax,pyramid(ax,1,0.5,3),1);Stereographic_projection(ax,points,1,'stereographic_projection_pyramid')"""},
       
                {'code': """points = normal_points(ax,bipyramid(ax,1,0.5,6),1);Stereographic_projection(ax,points,2,'stereographic_projection_bipyramid')"""},
    
                {'code': """points = normal_points(ax,prism(ax,2,2,6),2);Stereographic_projection(ax,points,2,'stereographic_projection_prism')"""},
          
                {'code': """points = normal_points(ax,biprismid(ax,3,1,0.5,5),1);Stereographic_projection(ax,points,2,'stereographic_projection_biprismid')"""},
                ]

    for stereo in stereos:
        fig = plt.figure(0,figsize=[8,8])
        ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
        code = stereo['code']
        exec(code)
    print('made all stereos')

################################################################################

#make_all_structure_gifs()
#make_all_operations_gifs()
#make_all_shape_gifs()
#make_all_face_norm_gifs()
make_all_stereos()

# fig = plt.figure(0,figsize=[8,8])
# ax = fig.add_subplot(111,projection='3d')
# faces = tetrakis(ax,4,1)
# #faces=bipyramid(ax,2,2,7)
# points=normal_points(ax,faces,10)
# Stereographic_projection(ax,points,10,'stereographic_projection_tetrakis')
# plt.show()