from PyCrystallography.structure import *

def primitive_cell_2d(cell_type):
    """
    """
    if cell_type == 'rhombus':
        x_points = [0,1,0.5,1.5]
        y_points = [0,0,1,1]

    if cell_type == 'square':
        x_points = [0,1,0,1]
        y_points = [0,0,1,0]

    else:
        print('"{}" is not a vaild uncit cell shape"'.format(cell_type))

    primitive_cell_2d =(x_points,y_points)
    return primitive_cell_2d

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