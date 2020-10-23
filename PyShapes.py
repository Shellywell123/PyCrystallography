import numpy as np
from PyCrystallography import plot_axis,make_atom,make_bond,plot_bonds,plot_atoms

def make_atom(x,y,z,siz,col):
    """
    creates a dict for an atoms pos in a structure
    """
    atom = {'x':   x,
            'y':   y,
            'z':   z,
            'size': siz,
            'color':col}
    return atom

def make_bond(x_list,y_list,z_list,siz,col):
    """
    creates a dict for an bonds pos in a structure
    """
    bond = {'x':   x_list,
            'y':   y_list,
            'z':   z_list,
            'size': siz,
            'color':col}
    return bond

def plot_bonds(ax,bonds):
    """
    plots all bonds in a struct using matplotlib line
    """

    for bond in bonds:
        x1,x2 = bond['x']
        y1,y2 = bond['y']
        z1,z2 = bond['z']
        col   = bond['color']
        siz   = bond['size']
        ax.plot([x1,x2],[y1,y2],[z1,z2],linewidth=siz,c=col)

def plot_atoms(ax,atoms):
    """
    plots all atoms in a struct using matplotlib scatter
    """

    for atom in atoms:
        x1,x2 = atom['x']
        y1,y2 = atom['y']
        z1,z2 = atom['z']
        col   = atom['color']
        siz   = atom['size']
        ax.plot([x1,x2],[y1,y2],[z1,z2],linewidth=siz,c=col)


def plot_axis(ax,max_lim=10):
    """
    will clear all amtplotlib axis defaults and draw custom axis centered at 000
    """
    ax.set_facecolor('white')
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

    ax.grid(False)

    min_lim = -max_lim
    ax.auto_scale_xyz([min_lim, max_lim],
                [min_lim, max_lim], 
                [min_lim, max_lim])   

    #make axes at orgin
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

def cuboid(ax,h,w,d):
    """
    will plot a cuboid of given height, width and depth in x,y, and z
    """
    bonds = []
    plot_axis(ax,max_lim=1*max(h,w,d))
    for i in [-h/2,h/2]:
        for j in [-w/2,w/2]:
            for k in [-d/2,d/2]:
                bonds.append(make_bond([-i,i],[j,j],[k,k],1,'k'))
                bonds.append(make_bond([i,i],[-j,j],[k,k],1,'k'))
                bonds.append(make_bond([i,i],[j,j],[-k,k],1,'k'))
    plot_bonds(ax,bonds)

def tetrakis(ax,h,dh):
    """
    will plot a tetrakis
    """
    bonds = []
    plot_axis(ax,max_lim=h)
    for i in [-1,1]:
        for j in [-1,1]:
            for k in [-1,1]:
                bonds.append(make_bond([-i*h/2,i*h/2],[j*h/2,j*h/2],[k*h/2,k*h/2],1,'k'))
                bonds.append(make_bond([i*h/2,i*h/2],[-j*h/2,j*h/2],[k*h/2,k*h/2],1,'k'))
                bonds.append(make_bond([i*h/2,i*h/2],[j*h/2,j*h/2],[-k*h/2,k*h/2],1,'k'))
                bonds.append(make_bond([i*h/2,i*(h/2+dh)] ,[j*h/2,0],[k*h/2,0],1,'k'))
                bonds.append(make_bond([i*h/2,0] ,[j*h/2,j*(h/2+dh)],[k*h/2,0],1,'k'))
                bonds.append(make_bond([i*h/2,0] ,[j*h/2,0],[k*h/2,k*(h/2+dh)],1,'k'))
    plot_bonds(ax,bonds)

def pyramid(ax,h,num_of_side):
    """
    will plot a pyramid with num of sides -1
    """
    bonds = []
    plot_axis(ax,max_lim=1.1*h)

    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi
        theta_next = (2*(n+1)/num_of_side)*np.pi
        x = h*np.cos(theta)
        y = h*np.sin(theta)

        x_next = h*np.cos(theta_next)
        y_next = h*np.sin(theta_next)

        bonds.append(make_bond([0,x] ,[0,y],[h/2,-h/2],1,'k'))
        bonds.append(make_bond([x,x_next] ,[y,y_next],[-h/2,-h/2],1,'k'))
    plot_bonds(ax,bonds)

def bipyramid(ax,h,num_of_side):
    """
    will plot a bipyramid with number of sides /2
    """
    bonds = []
    plot_axis(ax,max_lim=1.1*h)
    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi
        theta_next = (2*(n+1)/num_of_side)*np.pi
        x = h*np.cos(theta)
        y = h*np.sin(theta)

        x_next = h*np.cos(theta_next)
        y_next = h*np.sin(theta_next)

        bonds.append(make_bond([0,x] ,[0,y],[h/2,0],1,'k'))
        bonds.append(make_bond([x,x_next] ,[y,y_next],[0,0],1,'k'))
        bonds.append(make_bond([0,x] ,[0,y],[-h/2,0],1,'k'))
    plot_bonds(ax,bonds)

def prism(ax,h,num_of_side):
    """
    will plot a prism with number of sides /2
    """
    bonds =[]
    plot_axis(ax,max_lim=1.1*h)
    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi
        theta_next = (2*(n+1)/num_of_side)*np.pi
        x = h*np.cos(theta)
        y = h*np.sin(theta)

        x_next = h*np.cos(theta_next)
        y_next = h*np.sin(theta_next)

        bonds.append(make_bond([x,x] ,[y,y],[h/2,-h/2],1,'k'))
        bonds.append(make_bond([x,x_next] ,[y,y_next],[h/2,h/2],1,'k'))
        bonds.append(make_bond([x,x_next] ,[y,y_next],[-h/2,-h/2],1,'k'))
    plot_bonds(ax,bonds)

def biprismid(ax,h,dh,num_of_side):
    """
    will plot a bi-prism-id with number of sides /2
    """
    bonds = []
    plot_axis(ax,max_lim=1.1*h)
    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi
        theta_next = (2*(n+1)/num_of_side)*np.pi
        x = h*np.cos(theta)
        y = h*np.sin(theta)

        x_next = h*np.cos(theta_next)
        y_next = h*np.sin(theta_next)


        bonds.append(make_bond([0,x] ,[0,y],[h/2+dh,h/2],1,'k'))
        bonds.append(make_bond([x,x] ,[y,y],[h/2,-h/2],1,'k'))
        bonds.append(make_bond([x,x_next] ,[y,y_next],[h/2,h/2],1,'k'))
        bonds.append(make_bond([x,x_next] ,[y,y_next],[-h/2,-h/2],1,'k'))
        bonds.append(make_bond([0,x] ,[0,y],[-h/2-dh,-h/2],1,'k'))
    plot_bonds(ax,bonds)