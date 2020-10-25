import numpy as np

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

                if (abs(i)==abs(j)==abs(k)!=0)or(abs(i)+abs(j)+abs(k)==h/2):
                    COL ='green'
                    SIZ =50
                else:
                    COL = 'red'
                    SIZ = 20

                atoms.append(make_atom([i],[j],[k],SIZ,COL))
    
    plot_atoms(ax,atoms)
    plot_bonds(ax,bonds)

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

def invert(x,y,z,origin=[0,0,0]):
    """ 
    inverts a points around n origin
    """
    x_inv = -x + origin[0]
    y_inv = -y + origin[1]
    z_inv = -z + origin[2]
    return x_inv, y_inv, z_inv

def inversion(ax,h,w,d):
    """
    plots an annotated points being inversed through the orgin
    """
    plot_axis(ax,max_lim=1.1*max(h,w,d))
    pos = .1*max(h,w,d)

    h_inv,w_inv,d_inv = invert(h,w,d)
    ax.plot([h_inv,h],[w_inv,w],[d_inv,d],c='k',linestyle='--')
    ax.text(h+pos,w+pos,d+pos,r"$(x,y,z)$")
    ax.text(0,0,0,r"O[0,0]")
    ax.text(h_inv-pos,w_inv-pos,d_inv-pos,r"$-(x,y,z)$")

def reflection(ax,h,w,d):
    """
    plots a annotated point being mirrored in a plotted plane
    """
    plot_axis(ax,max_lim=1.1*max(h+3,w+3,d+3))

    pos = .1*max(h,w,d)
    ax.plot([h,h],[w,w],[-d,d],c='k',linestyle='--')
    ax.text(h+pos,w+pos,d+pos,r"$(x,y,z)$")
    ax.text(h-pos,w-pos,-d-pos,r"$(x',y',z')$")

    h = h+3
    w= w+3
    plane(ax,h,w,d,plane_axis='z')
    ax.text(h,w,0,r'm')

def plane(ax,h,w,d,plane_axis):
    """
    plots a plane in x,y or z
    """
    if plane_axis =='x':

        z = np.arange(-h,h,0.5)
        y = np.arange(-w,w,0.5)

        z,y = np.meshgrid(z,y)

        x =  np.zeros(z.shape)
        ax.plot_surface(x,y,z,alpha=0.5)

    if plane_axis =='y':
  
        x = np.arange(-h,h,0.5)
        z = np.arange(-w,w,0.5)

        x,z = np.meshgrid(x,z)

        y =  np.zeros(x.shape)
        ax.plot_surface(x,y,z,alpha=0.5)

    if plane_axis =='z':

        x = np.arange(-h,h,0.5)
        y = np.arange(-w,w,0.5)

        x,y = np.meshgrid(x,y)

        z =  np.zeros(x.shape)
        ax.plot_surface(x,y,z,alpha=0.5)


def rotation(ax,h,w,d):
    """
    """
    plot_axis(ax,max_lim=1.1*max(h,w,d))
    pass

def cube_reflection(ax,h,w,d):
    """
    cube with some internal refelctive planes plotted
    """
    plot_axis(ax,max_lim=1.1*max(h,w,d))
    from PyShapes import cuboid
    cuboid(ax,h,w,d)
    h=h/2
    w=w/2
    d=d/2
    plane(ax,h,w,d,'x')
    ax.text(0,w,d,r'm_1')
    plane(ax,h,w,d,'y')
    ax.text(h,0,d,r'm_2')
    plane(ax,h,w,d,'z')
    ax.text(h,w,0,r'm_3')

def test_sphere(ax):
    """
    test cube face normals to points on a sphere
    """
    plot_axis(ax)
    from PyShapes import cuboid
    cuboid(ax,3,3,3)
    x = [0,0,5,-5,0,0]
    y = [0,0,0,0,5,-5]
    z = [5,-5,0,0,0,0]
    ax.scatter(x,y,z,c='red')

    ax.plot([2,5],[0,0],[0,0],linestyle='--',c='k')
    ax.plot([0,0],[2,5],[0,0],linestyle='--',c='k')
    ax.plot([0,0],[0,0],[2,5],linestyle='--',c='k')
    ax.plot([-2,-5],[0,0],[0,0],linestyle='--',c='k')
    ax.plot([0,0],[-2,-5],[0,0],linestyle='--',c='k')
    ax.plot([0,0],[0,0],[-2,-5],linestyle='--',c='k')

    r = 5

    return x,y,z,r

def Stereographic_projection(ax,points,r,name):
    """
    takes x,y,z coords that all lie on the surface of a 
    sphere and outputs a 2d stereograph
    """
    x = []
    y = []
    z = []

    for vert in points:
        x.append(vert[0])
        y.append(vert[1])
        z.append(vert[2])

    x_ = []
    y_ = []

    import matplotlib.pyplot as plt

    fig = plt.figure(1,figsize=[8,8])

    for i in range(0,len(x)):
        x_.append(x[i]/(1-z[i]))
        y_.append(y[i]/(1-z[i]))

        if z[i] > 0:
            plt.scatter(x_[i],y_[i],marker='2',label='N',c='blue',s=200)
        else:
            plt.scatter(x_[i],y_[i],marker='1',label='S',c='r',s=200)

    theta = np.linspace(0,2*np.pi,100)
    xc = (r+1)*np.cos(theta)
    yc = (r+1)*np.sin(theta)

    ## sort leg
    north = plt.scatter([],[],marker='2',label='Northern Hemisphere',c='blue',s=200)
    south = plt.scatter([],[],marker='2',label='Southern Hemisphere',c='r',s=200)

    plt.legend(handles=[north,south],bbox_to_anchor=(0., 1.01, 1., .101), loc='lower left',
         mode="expand", borderaxespad=0.)
    plt.tight_layout(pad=0, h_pad=0, w_pad=0,rect=[0,0,0.95,0.95])
    plt.plot(xc,yc,c='k')
    plt.axis('off')
    plt.xlim([-r-1,r+1])
    plt.ylim([-r-1,r+1])
    plt.savefig('Images/{}.png'.format(name))
    #plt.show()
