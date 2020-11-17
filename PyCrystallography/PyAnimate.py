import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PyShapes import *
from PyCrystallography import *
from PyPacking import *

###############################################################################
# gif making functions
################################################################################

def delete_all_frames():
    """
    """
    os.system('rm Images/frames/*')

################################################################################

def save_frame(frame,num_of_frames):
    """
    """
    if frame <= 8:
        frame = '0'+str(frame+1)
    else:
        frame = str(frame+1)

    filename = 'Images/frames/{}_{}.png'.format(frame,num_of_frames)
    plt.savefig(filename)
    print(' - Frame ({}/{}) Saved.'.format(frame,num_of_frames))
    return filename

################################################################################

def frames_to_gif(filename,name):
    """
    """
    # convert all saved images to a single gif
    import imageio
    images = []
    for filename in os.listdir('Images/frames/'):
        images.append(imageio.imread('Images/frames/'+filename))
    imageio.mimsave('Images/{}.gif'.format(name), images) 
    print('{}.gif made'.format(name))

################################################################################

def objects_to_spin_gif(objects):
    """
    """

    for object in objects:
        delete_all_frames()
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

            filename = save_frame(frame,num_of_frames)

        frames_to_gif(filename,name)

################################################################################

def objects_to_n_gif(objects,n_max):
    """
    """
    for object in objects:
        delete_all_frames()
        
        code = object['code']
        name = object['name']

        for n in range(0,n_max):
            fig = plt.figure(0,figsize=[8,8])
            fig.clear()

            exec(code)

            filename = save_frame(n,n_max)

        frames_to_gif(filename,name)

################################################################################
# code to gifs
################################################################################

def make_all_structure_gifs():
    """
    generates screenshots of the program and then compiles them into a gif
    """

    objects = [
                {'code'     : 'FCC(ax)',
                 'name'     : 'FCC_unit_cell'},

                {'code'     : 'BCC(ax)',
                 'name'     : 'BCC_unit_cell'},

                {'code'     : 'NaCl(ax)',
                 'name'     : 'NaCl_unit_cell'},

                {'code'     : 'Diamond(ax)',
                 'name'     : 'diamond_unit_cell'}
                ]

    objects_to_spin_gif(objects)

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

    objects_to_spin_gif(objects)

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

    objects_to_spin_gif(objects)

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

    objects_to_spin_gif(objects)

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

    frames_to_gif(filename,name)

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

        filename = save_frame(frame,num_of_frames)

    frames_to_gif(filename,name)

################################################################################

def make_all_packing_gifs():
    """
    """

    objects = [
                {'code'    : 'ax = fig.add_subplot(111,projection="3d",azim=30,elev=30);prim = Diamond(ax);fig = plt.figure(0,figsize=[8,8]);fig.clear();ax = fig.add_subplot(111,projection="3d",azim=30,elev=30);make_lattice_3d(ax,prim,depth = n)',
                 'name'    : 'diamond_lattice'},

                {'code'    : 'ax = fig.add_subplot(111,projection="3d",azim=30,elev=30);prim = BCC(ax);fig = plt.figure(0,figsize=[8,8]);fig.clear();ax = fig.add_subplot(111,projection="3d",azim=30,elev=30);make_lattice_3d(ax,prim,depth = n)',
                 'name'    : 'BCC_lattice'},

                {'code'    : 'ax = fig.add_subplot(111,projection="3d",azim=30,elev=30);prim = FCC(ax);fig = plt.figure(0,figsize=[8,8]);fig.clear();ax = fig.add_subplot(111,projection="3d",azim=30,elev=30);make_lattice_3d(ax,prim,depth = n)',
                 'name'    : 'FCC_lattice'},

                {'code'    : 'ax = fig.add_subplot(111,projection="3d",azim=30,elev=30);prim = NaCl(ax);fig = plt.figure(0,figsize=[8,8]);fig.clear();ax = fig.add_subplot(111,projection="3d",azim=30,elev=30);make_lattice_3d(ax,prim,depth = n)',
                 'name'    : 'NaCl_lattice'},

                {'code'    : 'triangle_subdivision(n,"diag")',
                 'name'    : 'triangle_subdivision_diag'},

                {'code'    : 'triangle_subdivision(n,"zelda")',
                 'name'    : 'triangle_subdivision_zelda'},

                {'code'    : 'triangle_subdivision(n."grid")',
                 'name'    : 'triangle_subdivision_grid'},

                {'code'    : 'Penrose_Tiling(n,"sun")',
                 'name'    : 'penrose_tiling_sun'},

                {'code'    : 'Penrose_Tiling(n,"star")',
                 'name'    : 'penrose_tiling_star'},

                {'code'    : 'prim = primitive_cell_2d("square");make_lattice_2d(prim,depth=n)',
                 'name'    : 'square_lattice'},

                {'code'    : 'prim = primitive_cell_2d("rhombus");make_lattice_2d(prim,depth=n)',
                 'name'    : 'rhombus_lattice'}
                ]

    objects_to_n_gif(objects,7)

################################################################################

def make_all_miller_gifs():
    """
    """

    objects = [
            {'code'    : 'miller_indicies(ax,"<100>")',
             'name'    : 'miller_100'},

            {'code'    : 'miller_indicies(ax,"<010>")',
             'name'    : 'miller_010'},

            {'code'    : 'miller_indicies(ax,"<001>")',
             'name'    : 'miller_001'},

            {'code'    : 'miller_indicies(ax,"<110>")',
             'name'    : 'miller_110'},

            {'code'    : 'miller_indicies(ax,"<101>")',
             'name'    : 'miller_101'},

            {'code'    : 'miller_indicies(ax,"<011>")',
             'name'    : 'miller_011'},

            {'code'    : 'miller_indicies(ax,"<111>")',
             'name'    : 'miller_111'},

            {'code'    : 'cube_reflection(ax)',
             'name'    : 'cube_reflection'},

            {'code'    : 'cube_reflection_diag(ax)',
             'name'    : 'cube_reflection_diag'}
            ]

    objects_to_spin_gif(objects)

################################################################################

make_all_structure_gifs()
make_all_operations_gifs()
make_all_shape_gifs()
make_all_face_norm_gifs()
make_all_stereos()
make_all_stereo_gifs()
make_all_packing_gifs()
make_all_miller_gifs()