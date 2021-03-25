from PyCrystallography.structure import *
import numpy as np

def primitive_cell_2d(cell_type):
    """
    """
    if cell_type == 'triangle':
        r_uc = 1.2

        x_points = []
        y_points = []

        dtheta_uc = 2*np.pi/3
        for i in range(0,3):
            ang = i*dtheta_uc+dtheta_uc/2
            x_points.append(r_uc*np.sin(ang)+r_uc)
            y_points.append(r_uc*np.cos(ang)+r_uc)

    elif cell_type == 'rhombus':
        x_points = [0,1,0.5,1.5]
        y_points = [0,0,1,1]

    elif cell_type == 'square':
        x_points = [0,1,0,1]
        y_points = [0,0,1,0]

    elif cell_type == 'hexagon':
        r_uc = 1

        x_points = []
        y_points = []

        dtheta_uc = 2*np.pi/6
        for i in range(0,6):
            ang = i*dtheta_uc#+dtheta_uc/2
            x_points.append(r_uc*np.sin(ang))
            y_points.append(r_uc*np.cos(ang))


    else:
        print('"{}" is not a vaild uncit cell shape"'.format(cell_type))

    primitive_cell_2d =(x_points,y_points)
    return primitive_cell_2d

def custom_unit_cell(ax,vectors):
    """
    create unit cell atom and bonds from primitive vectors
    """

    A,B,C = vectors
    vector_A_x,vector_A_y,vector_A_z = A
    vector_B_x,vector_B_y,vector_B_z = B
    vector_C_x,vector_C_y,vector_C_z = C

    x_d =max(vector_A_x,vector_B_x,vector_C_x)+min(vector_A_x,vector_B_x,vector_C_x)
    y_d =max(vector_B_y,vector_B_y,vector_C_y)+min(vector_B_y,vector_B_y,vector_C_y)
    z_d =max(vector_A_z,vector_B_z,vector_C_z)+min(vector_A_z,vector_B_z,vector_C_z)

    dim = max(x_d,y_d,z_d)
    bonds = []
    atoms = []

    plot_axis(ax,max_lim=0.5*dim)
    for i in [-x_d/2,x_d/2]:
        for j in [-y_d/2,y_d/2]:
            for k in [-z_d/2,z_d/2]:
                bonds.append(make_bond([-i,i],[j,j],[k,k],1,'k'))
                bonds.append(make_bond([i,i],[-j,j],[k,k],1,'k'))
                bonds.append(make_bond([i,i],[j,j],[-k,k],1,'k'))

                COL ='red'
                SIZ =50

                atoms.append(make_atom([i,i],[j,j],[k,k],SIZ,COL))

    primitive_cell = (atoms,bonds)
    return primitive_cell


def Cubic(ax):
    """
    plot the cubic primitive cell
    """

    h =2
    w =2
    d =2

    dim = max(h,w,d)
    bonds = []
    atoms = []

    plot_axis(ax,max_lim=0.5*dim)
    for i in [-h/2,h/2]:
        for j in [-w/2,w/2]:
            for k in [-d/2,d/2]:
                bonds.append(make_bond([-i,i],[j,j],[k,k],1,'k'))
                bonds.append(make_bond([i,i],[-j,j],[k,k],1,'k'))
                bonds.append(make_bond([i,i],[j,j],[-k,k],1,'k'))

                COL ='red'
                SIZ =50

                atoms.append(make_atom([i,i],[j,j],[k,k],SIZ,COL))

    #plot_atoms(ax,atoms)
    #plot_bonds(ax,bonds)

    primitive_cell = (atoms,bonds)
    return primitive_cell

def BCC(ax):
    """
    plot the body centered cubic primitive cell
    """

    h =2
    w =2
    d =2
    bonds = []
    atoms = []

    plot_axis(ax,max_lim=0.5*max(h,w,d))
    for i in [-h/2,h/2]:
        for j in [-w/2,w/2]:
            for k in [-d/2,d/2]:
                bonds.append(make_bond([-i,i],[j,j],[k,k],1,'k'))
                bonds.append(make_bond([i,i],[-j,j],[k,k],1,'k'))
                bonds.append(make_bond([i,i],[j,j],[-k,k],1,'k'))

                COL ='red'
                SIZ =50

                atoms.append(make_atom([i,i],[j,j],[k,k],SIZ,COL))
    atoms.append(make_atom([0],[0],[0],SIZ,COL))
    plot_atoms(ax,atoms)
    plot_bonds(ax,bonds)

    primitive_cell = (atoms,bonds)
    return primitive_cell


def FCC(ax):
    """
    plots the face centred cubic primitive cell
    """

    h =2
    w =2
    d =2
    bonds = []
    atoms = []
    plot_axis(ax,max_lim=0.5*max(h,w,d))
    for i in [-h/2,h/2]:
        for j in [-w/2,w/2]:
            for k in [-d/2,d/2]:
                bonds.append(make_bond([-i,i],[j,j],[k,k],1,'k'))
                bonds.append(make_bond([i,i],[-j,j],[k,k],1,'k'))
                bonds.append(make_bond([i,i],[j,j],[-k,k],1,'k'))

                COL ='red'
                SIZ =50

                atoms.append(make_atom([i],[j],[k],SIZ,COL))
                atoms.append(make_atom([0],[0],[k],SIZ,COL))
                atoms.append(make_atom([0],[j],[0],SIZ,COL))
                atoms.append(make_atom([i],[0],[0],SIZ,COL))
    plot_atoms(ax,atoms)
    plot_bonds(ax,bonds)

    primitive_cell = (atoms,bonds)
    return primitive_cell

def NaCl(ax):
    """
    plots the nacl atom structure
    """

    h =2
    w =2
    d =2
    bonds = []
    atoms = []
    plot_axis(ax,max_lim=0.7*max(h,w,d))
    for i in [-h/2,0,h/2]:
        for j in [-w/2,0,w/2]:
            for k in [-d/2,0,d/2]:
                bonds.append(make_bond([-i,i],[j,j],[k,k],1,'k'))
                bonds.append(make_bond([i,i],[-j,j],[k,k],1,'k'))
                bonds.append(make_bond([i,i],[j,j],[-k,k],1,'k'))

                if (abs(i)==abs(j)==abs(k)!=0) or (abs(i)+abs(j)+abs(k)==h/2):
                    COL ='green'
                    SIZ =50
                else:
                    COL = 'red'
                    SIZ = 20

                atoms.append(make_atom([i],[j],[k],SIZ,COL))
    
    plot_atoms(ax,atoms)
    plot_bonds(ax,bonds)

    primitive_cell = (atoms,bonds)
    return primitive_cell

def Diamond(ax):
    """
    plots the diamond atom structure
    """
    h =2
    w =2
    d =2
    bonds = []
    atoms = []
    plot_axis(ax,max_lim=0.9*max(h,w,d))
    for i in [-h/2,h/2]:
        for j in [-w/2,w/2]:
            for k in [-d/2,d/2]:

                COL ='red'
                SIZ =50
                if i+j+k==h/2:
                    atoms.append(make_atom([i],[j],[k],SIZ,COL))
                atoms.append(make_atom([0],[0],[k],SIZ,COL))
                atoms.append(make_atom([0],[j],[0],SIZ,COL))
                atoms.append(make_atom([i],[0],[0],SIZ,COL))

    atoms.append(make_atom([-h/2],[-h/2],[-h/2],SIZ,COL))

    atoms.append(make_atom([-h/4],[-h/4],[-h/4],SIZ,COL))
    atoms.append(make_atom([h/4],[h/4],[-h/4],SIZ,COL))
    atoms.append(make_atom([-h/4],[h/4],[h/4],SIZ,COL))
    atoms.append(make_atom([h/4],[-h/4],[h/4],SIZ,COL))

    bonds.append(make_bond([-h/2,-h/4],[-h/2,-h/4],[-h/2,-h/4],1,'k'))
    bonds.append(make_bond([h/2,h/4],[h/2,h/4],[-h/2,-h/4],1,'k'))

    bonds.append(make_bond([-h/2,-h/4],[h/2,h/4],[h/2,h/4],1,'k'))
    bonds.append(make_bond([h/2,h/4],[-h/2,-h/4],[h/2,h/4],1,'k'))

    bonds.append(make_bond([-h/2,-h/4],[0,h/4],[0,h/4],1,'k'))
    bonds.append(make_bond([h/2,h/4],[0,-h/4],[0,h/4],1,'k'))

    bonds.append(make_bond([0,-h/4],[-h/2,-h/4],[0,-h/4],1,'k'))
    bonds.append(make_bond([0,-h/4],[h/2,h/4],[0,h/4],1,'k'))

    bonds.append(make_bond([-h/2,-h/4],[0,-h/4],[0,-h/4],1,'k'))
    bonds.append(make_bond([h/2,h/4],[0,h/4],[0,-h/4],1,'k'))

    bonds.append(make_bond([0,h/4],[-h/2,-h/4],[0,h/4],1,'k'))
    bonds.append(make_bond([0,h/4],[h/2,h/4],[0,-h/4],1,'k'))

    bonds.append(make_bond([-h/4,0],[-h/4,0],[-h/4,-h/2],1,'k'))
    bonds.append(make_bond([-h/4,0],[h/4,0],[h/4,h/2],1,'k'))

    bonds.append(make_bond([h/4,0],[h/4,0],[-h/4,-h/2],1,'k'))
    bonds.append(make_bond([h/4,0],[-h/4,0],[h/4,h/2],1,'k'))

    plot_atoms(ax,atoms)
    plot_bonds(ax,bonds)

    primitive_cell = (atoms,bonds)
    return primitive_cell