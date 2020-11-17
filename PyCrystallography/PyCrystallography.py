import numpy as np

#########################################
# symmetry
#########################################

def identify_fold_symmetry(n_points,e_points,s_points):
    """
    going to be a function that check the circle of which a point lies  on stereo proj  on to count all other points on that circle and return that as th en fold symm
    if only one point.
    """
    nfold_results = []
    for points in [n_points,e_points,s_points]:
        if points == n_points:
            print('\nN-hemi {} points'.format(len(points)))
        else:
            print('\nS-hemi {} points'.format(len(points)))
        print('radius,theta_sum,theta,mean,checkval')

        polar_coords = []
        
        for point in points:

            # get points radial coord
            # count how many other points lie on a circle of the same radius
            # gruop points by radial dist and check the al have same n fold (igrore points at origin)
            # return count
         #   print(point)
            x = point[0]
            y = point[1]
            r = np.sqrt(x**2 + y**2)
            theta = np.arctan(y/x)
          #  if theta == -0.0:
           #     theta = np.pi
            if theta < 0 :
                theta = 2*np.pi+theta
            if np.isnan(theta) == True:
                theta = 0.0
            polar_coords.append([r,theta])

        #leave 0 in list as it can be folded any way
        checked_rs = [0]

        #generate list of radii
        list_of_r = []
        for point in polar_coords:
            list_of_r.append(point[0])

        polar_coords_copy = polar_coords

        # search for raddii indexs and use that to check angles of set radial dists
        for i in range(0,len(polar_coords_copy)):
            current_r = polar_coords[i][0]
            if current_r not in checked_rs:
               # print(current_r)
                searchval = current_r
             #   print(list_of_r)
                indexs = np.where(list_of_r == searchval)[0]
                checked_rs.append(current_r)

                #current method for checking nfold is 
                # that the mean angle should = 2pi/nfold, for nfold num of points
                theta_sum = 0
                for index in indexs:
                    current_theta = polar_coords[index][1]
               #     print(current_r,current_theta)
                    theta_sum = theta_sum + current_theta

                theta_mean = theta_sum/len(indexs)    

                if theta_mean > np.pi:
                    theta_mean = 2*(theta_mean-np.pi)           

               # print(current_r,theta_sum,theta_mean,2*np.pi/len(indexs),len(indexs))

                if theta_mean == 2*np.pi/len(indexs):
                 #   print(indexs)
                    result =len(indexs)
                    nfold_results.append(result)
            else:
                pass

        if all(element == nfold_results[0] for element in nfold_results):
            print('NFOLD = ',nfold_results[0])


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

#########################################
# operatoins
#########################################

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

    plane_verts = [[h,-w,0],[-h,-w,0],[-h,w,0],[h,w,0]]
    from PyShapes import plot_face
    plot_face(ax,plane_verts,color='C0')
    ax.text(h,w,0,r'm')

def rotation(ax,h,w,d):
    """
    """
    plot_axis(ax,max_lim=1.1*max(h,w,d))
    pass

def miller_indicies(ax,index):
    """
    """

    if index == '<100>':
        verts = [[1,-1,-1],[1,1,-1],[1,1,1],[1,-1,1]]

    if index == '<010>':
        verts = [[-1,1,-1],[1,1,-1],[1,1,1],[-1,1,1]]
  
    if index == '<001>':
        verts = [[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]]
        
    if index == '<110>':
        verts = [[-1,1,1],[1,-1,1],[1,-1,-1],[-1,1,-1]]

    if index == '<101>':
        verts = [[-1,-1,1],[-1,1,1],[1,1,-1],[1,-1,-1]]

    if index == '<011>':
        verts = [[-1,-1,1],[1,-1,1],[1,1,-1],[-1,1,-1]]

    if index == '<111>':
        verts = [[0,0,1],[0,1,0],[1,0,0]]

    from PyShapes import cuboid
    cuboid(ax,2,2,2,alpha=0.01,show_axis=False)
    ax.plot([-1, 1],[-1,-1],[-1,-1],c='r',label='V1',linewidth=5)
    ax.plot([-1,-1],[-1, 1],[-1,-1],c='b',label='V2',linewidth=5)
    ax.plot([-1,-1],[-1,-1],[-1, 1],c='g',label='V3',linewidth=5)

    from PyShapes import plot_face
    plot_face(ax,verts,color='pink')
    ax.plot([],[],[],c='pink',label=index)

    ax.legend()
    ax.axis('off')

def cube_reflection(ax):
    """
    cube with some internal refelctive planes plotted
    """

    from PyShapes import cuboid
    cuboid(ax,2,2,2,alpha=0.01)

    verts_100 = [[0,-1,-1],[0,1,-1],[0,1,1],[0,-1,1]]
    verts_010 = [[-1,0,-1],[1,0,-1],[1,0,1],[-1,0,1]]
    verts_001 = [[-1,-1,0],[1,-1,0],[1,1,0],[-1,1,0]]

    from PyShapes import plot_face

    plot_face(ax,verts_100,color='red')
    ax.plot([],[],[],c='red',label='<100>')

    plot_face(ax,verts_010,color='green')
    ax.plot([],[],[],c='green',label='<010>')

    plot_face(ax,verts_001,color='blue')
    ax.plot([],[],[],c='blue',label='<001>')

    ax.legend()

def cube_reflection_diag(ax):
    """
    cube with some internal refelctive planes plotted
    """
    from PyShapes import cuboid
    cuboid(ax,2,2,2,alpha=0.01)

    verts_110 = [[-1,1,1],[1,-1,1],[1,-1,-1],[-1,1,-1]]
    verts_101 = [[-1,-1,1],[-1,1,1],[1,1,-1],[1,-1,-1]]
    verts_011 = [[-1,-1,1],[1,-1,1],[1,1,-1],[-1,1,-1]]

    from PyShapes import plot_face

    plot_face(ax,verts_110,color='yellow')
    ax.plot([],[],[],c='yellow',label='<110>')

    plot_face(ax,verts_101,color='orange')
    ax.plot([],[],[],c='orange',label='<010>')

    plot_face(ax,verts_011,color='purple')
    ax.plot([],[],[],c='purple',label='<001>')

    ax.legend()

#########################################
# stereo projs
#########################################

def Stereographic_projection(points,r,name):
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

    n_points = []
    e_points = []
    s_points = []

    import matplotlib.pyplot as plt

    fig = plt.figure(1,figsize=[8,8])
    fig.clear()

    for i in range(0,len(x)):
        # x_.append(x[i]/(r-z[i]))
        # y_.append(y[i]/(r-z[i]))  
        if z[i] > 0:
            x_.append(x[i]/(r+z[i]))
            y_.append(y[i]/(r+z[i])) 
            n_points.append([x_[i],y_[i]])
            plt.scatter(x_[i],y_[i],marker='2',label='N',c='blue',s=200)
        elif z[i] == 0:
            x_.append(x[i]/(r+z[i]))
            y_.append(y[i]/(r+z[i])) 
            e_points.append([x_[i],y_[i]])
            plt.scatter(x_[i],y_[i],marker='+',label='E',c='green',s=200)
        else:
            x_.append(x[i]/(r-z[i]))
            y_.append(y[i]/(r-z[i]))
            s_points.append([x_[i],y_[i]])
            plt.scatter(x_[i],y_[i],marker='1',label='S',c='r',s=200)

     #   print(x_[i])
    theta = np.linspace(0,2*np.pi,100)

  #  r = np.sqrt(max(x_)**2 + max(y_)**2)
    pos =0.15*r
    xc = (r+pos)*np.cos(theta)
    yc = (r+pos)*np.sin(theta)

    ## sort leg
    north   = plt.scatter([],[],marker='2',label='Northern Hemisphere',c='blue',s=200)
    equator = plt.scatter([],[],marker='+',label='Equator',c='green',s=200)
    south   = plt.scatter([],[],marker='1',label='Southern Hemisphere',c='r',s=200)

    plt.legend(handles=[north,equator,south],bbox_to_anchor=(0., 1.01, 1., .101), loc='lower left',
         mode="expand")
    
    plt.plot(xc,yc,c='k')
    plt.xlim([-r-pos,r+pos])
    plt.ylim([-r-pos,r+pos])
    plt.tight_layout(pad=0, h_pad=0, w_pad=0,rect=[0,0,0.95,0.95])
    plt.axis('off')


    plt.savefig('Images/{}.png'.format(name))
    return n_points, e_points, s_points
