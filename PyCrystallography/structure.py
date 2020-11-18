
#########################################
# structures
#########################################

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
        x   = atom['x']
        y   = atom['y']
        z   = atom['z']
        col = atom['color']
        siz = atom['size']
        ax.scatter(x,y,z,s=siz,c=col)

def plot_face(ax,verts,alpha=0.5,color='C0'):
    """
    """

    x_list = []
    y_list = []
    z_list = []

    for vert in verts:
        x_list.append(vert[0])
        y_list.append(vert[1])
        z_list.append(vert[2])

    verts = [list(zip(x_list,y_list,z_list))]

    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    ax.add_collection3d(Poly3DCollection(verts,linewidths=1,color=color,edgecolor='k',alpha=alpha))


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