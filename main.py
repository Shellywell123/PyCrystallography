import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PyShapes import *
from PyCrystallography import *

################################################################################

def delete_all_frames():
    """
    """
    os.system('rm Images/frames/*')

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
                 'name'    : 'reflection'},

                {'code'    : 'cube_reflection(ax)',
                 'name'    : 'cube_reflection'},

                {'code'    : 'cube_reflection_diag(ax)',
                 'name'    : 'cube_reflection_diag'}
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

                {'code'    : 'normal_points(ax,biprismid(ax,3,1,0.5,5),3)',
                 'name'    : 'face_normals_biprismid'},

                {'code'    : 'normal_points(ax,tetrakis(ax,4,1),10)',
                 'name'    : 'face_normals_tetrakis'}
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
                 'name'    : 'tetrakis'}
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
                {'code': """points = normal_points(ax,cuboid(ax,2,2,2),2);Stereographic_projection(points,2,'stereographic_projection_cube')"""},
       
                {'code': """points = normal_points(ax,pyramid(ax,1,0.5,3),1);Stereographic_projection(points,1,'stereographic_projection_pyramid')"""},
       
                {'code': """points = normal_points(ax,bipyramid(ax,1,0.5,6),1);Stereographic_projection(points,2,'stereographic_projection_bipyramid')"""},
    
                {'code': """points = normal_points(ax,prism(ax,2,2,6),2);Stereographic_projection(points,2,'stereographic_projection_prism')"""},
          
                {'code': """points = normal_points(ax,biprismid(ax,3,1,0.5,5),1);Stereographic_projection(points,2,'stereographic_projection_biprismid')"""},
     
                {'code': """points = normal_points(ax,tetrakis(ax,4,1),10);Stereographic_projection(points,4,'stereographic_projection_tetrakis')"""}
                  ]

    for stereo in stereos:
        fig = plt.figure(0,figsize=[8,8])
        ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
        code = stereo['code']
        exec(code)
    print('made all stereos')

################################################################################

def make_all_stereo_gifs():
    """
    """
    delete_all_frames()
    name = 'stereographic_projection_inversion'
    r=1
    points = []
    d_theta = np.pi
    fig = plt.figure(0,figsize=[8,8])
    fig.clear()
    ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
    points.append([r*np.cos(d_theta),r*np.sin(d_theta),0])

    filename = 'frames/01_2'
    Stereographic_projection(points,r,filename)
    print('Frame (01/2) Saved.')

    # # # # # # # # # #

    fig = plt.figure(0,figsize=[8,8])
    fig.clear()
    ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
    x_inv,y_in,z_inv =invert(points[0][0],points[0][1],points[0][2])
    points.append([x_inv,y_in,z_inv])
    print(points)

    filename = 'frames/02_2'
    Stereographic_projection(points,r,filename)
    print('Frame (02/2) Saved.')

    # convert all saved images to a single gif
    import imageio
    images = []
    for filename in os.listdir('Images/frames/'):
        images.append(imageio.imread('Images/frames/'+filename))
    imageio.mimsave('Images/{}.gif'.format(name), images)
    print('{}.gif made'.format(name))

    #########################################
    #########################################

    delete_all_frames()
    name = 'stereographic_projection_rotation'
    n=10
    r=1
    points = []
    d_theta = 2*np.pi/n
    for i in range(0,n):
        fig = plt.figure(0,figsize=[8,8])
        fig.clear()
        ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
        points.append([r*np.cos(d_theta*i),r*np.sin(d_theta*i),0])

        if i <= 8:
            i = '0'+str(i+1)
        else:
            i = str(i+1)

        filename = 'frames/{}_{}'.format(i,n)
        Stereographic_projection(points,r,filename)
        print('Frame ({}/{}) Saved.'.format(i,n))

    # convert all saved images to a single gif
    import imageio
    images = []
    for filename in os.listdir('Images/frames/'):
        images.append(imageio.imread('Images/frames/'+filename))
    imageio.mimsave('Images/{}.gif'.format(name), images)
    print('{}.gif made'.format(name))

################################################################################

# make_all_structure_gifs()
# make_all_operations_gifs()
# make_all_shape_gifs()
# make_all_face_norm_gifs()
make_all_stereos()
# make_all_stereo_gifs()

fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d')
#faces = cuboid(ax,2,2,2)
#reflection(ax,2,2,2)
faces=biprismid(ax,3,1,0.5,5)
points=normal_points(ax,faces,5)
#print(points)

ns,ss=Stereographic_projection(points,3,'test')
#print(ns,ss)
identify_fold_symmetry(ns,ss)
#plt.show()