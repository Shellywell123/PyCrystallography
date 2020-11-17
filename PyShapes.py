import numpy as np
from PyCrystallography import plot_axis,make_atom,make_bond,plot_bonds,plot_atoms

def normal_points(ax,faces,r):
    """
    """

    sphere_points = []

    for face in faces:

        points_sum = np.array([0,0,0])

        for vert in face:
            points_sum = points_sum + vert

        face_centre = points_sum/len(face)


        vert1 = face[0]
        vert2 = face[1]
        vert3 = face[2]

        vec1 = [vert2[0]-vert1[0],vert2[1]-vert1[1],vert2[2]-vert1[2]]
        vec2 = [vert3[0]-vert1[0],vert3[1]-vert1[1],vert3[2]-vert1[2]]

        normal = np.cross(vec1,vec2)
      #  print(normal)
        
        # generate projected point on a sphere of radius r
        normal = face_centre+normal

        # scale to be on sphere
        current_r = np.sqrt(normal[0]**2 + normal[1]**2 + normal[2]**2)
       
        normal = normal * r/current_r

        current_r = np.sqrt(normal[0]**2 + normal[1]**2 + normal[2]**2)
       # print(current_r)

        if normal[2] > 0:
            COL ='blue'
        elif normal[2] == 0:
            COL ='green'
        else:
            COL='r'

        sphere_points.append(normal)
        ax.plot([face_centre[0],normal[0]],[face_centre[1],normal[1]],[face_centre[2],normal[2]],linewidth=3,c='k')
        ax.scatter(normal[0],normal[1],normal[2],linewidth=3,c=COL)

    return sphere_points

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
    ax.add_collection3d(Poly3DCollection(verts,linewidths=1,edgecolor='k',alpha=alpha,color=color))

def cuboid(ax,h,w,d,alpha=0.5,show_axis=True):
    """
    """
    if show_axis == True:
        plot_axis(ax,max_lim=1.5*max(h,w,d))
    faces = []

    #+w
    side_verts1 = [h/2,w/2,-d/2],[-h/2,w/2,-d/2],[-h/2,w/2,d/2],[h/2,w/2,d/2]
    faces.append(side_verts1)

    #-w
    side_verts2 = [h/2,-w/2,d/2],[-h/2,-w/2,d/2],[-h/2,-w/2,-d/2],[h/2,-w/2,-d/2]

    faces.append(side_verts2)

    #+h
    side_verts3 = [h/2,w/2,d/2],[h/2,-w/2,d/2],[h/2,-w/2,-d/2],[h/2,w/2,-d/2]
    faces.append(side_verts3)

    #-h
    side_verts4 = [-h/2,w/2,-d/2],[-h/2,-w/2,-d/2],[-h/2,-w/2,d/2],[-h/2,w/2,d/2]
    faces.append(side_verts4)

    #+d
    top_verts = [h/2,w/2,d/2],[-h/2,w/2,d/2],[-h/2,-w/2,d/2],[h/2,-w/2,d/2]
    faces.append(top_verts)

    #-d
    bottom_verts = [h/2,-w/2,-d/2],[-h/2,-w/2,-d/2],[-h/2,w/2,-d/2],[h/2,w/2,-d/2]

    faces.append(bottom_verts)

    for face in faces:
        plot_face(ax,face,alpha=alpha)

    return faces


def prism(ax,h_z,r_xy,num_of_side):
    """
    will plot a prism of given height, width and depth in x,y, and z
    """
    h = h_z
    r = r_xy

    plot_axis(ax,max_lim=1.5*max(h_z,r_xy))

    faces = []

    top_verts    = []
    bottom_verts = []

    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi + np.pi/4
        theta_next = (2*(n+1)/num_of_side)*np.pi+ np.pi/4

        x = (r)*np.cos(theta)
        y = (r)*np.sin(theta)

        x_next = (r)*np.cos(theta_next)
        y_next = (r)*np.sin(theta_next)

        side_verts = [x,y,-h/2],[x_next,y_next,-h/2],[x_next,y_next,h/2],[x,y,h/2]
        faces.append(side_verts)

        top_verts.append([x,y,h/2])
        bottom_verts.append([x,y,-h/2])

    faces.append(top_verts)
    faces.append(bottom_verts[::-1])

    for face in faces:
        plot_face(ax,face)

    return faces

def tetrakis(ax,r,dr):
    """
    will plot a tetrakis
    """
    faces = []

    top_verts    = []
    bottom_verts = []

    plot_axis(ax,max_lim=1.1*(r+2*dr))
    for n in range(0,4):
        theta      = (2*n/4)*np.pi + np.pi/4
        theta_next = (2*(n+1)/4)*np.pi+ np.pi/4
        theta_mid  = (2*(n+0.5)/4)*np.pi+ np.pi/4

        x = (r)*np.cos(theta)
        y = (r)*np.sin(theta)

        x_mid = (r+dr)*np.cos(theta_mid)
        y_mid = (r+dr)*np.sin(theta_mid)
        z_mid = 0

        x_next = (r)*np.cos(theta_next)
        y_next = (r)*np.sin(theta_next)

        h = 2*r*np.sin(np.pi/4)

        side_verts_top = [0,0,h/2+dr],[x,y,h/2],[x_next,y_next,h/2]
        faces.append(side_verts_top)

        side_verts_mid_up = [x_mid,y_mid,z_mid],[x_next,y_next,h/2],[x,y,h/2]

        faces.append(side_verts_mid_up)

        side_verts_mid_left = [x_mid,y_mid,z_mid],[x,y,h/2],[x,y,-h/2]
        faces.append(side_verts_mid_left)

        side_verts_mid_right = [x_next,y_next,-h/2],[x_next,y_next,h/2],[x_mid,y_mid,z_mid]
        faces.append(side_verts_mid_right)

        side_verts_mid_down = [x,y,-h/2],[x_next,y_next,-h/2],[x_mid,y_mid,z_mid]
        faces.append(side_verts_mid_down)

        side_verts_bottom = [x_next,y_next,-h/2],[x,y,-h/2],[0,0,-h/2-dr]
        faces.append(side_verts_bottom)

    for face in faces:
        plot_face(ax,face)

    return faces

def pyramid(ax,h,r,num_of_side):
    """
    will plot a pyramid with num of sides -1
    """
    faces = []
    bottom_verts = []
    plot_axis(ax,max_lim=1.1*h)

    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi
        theta_next = (2*(n+1)/num_of_side)*np.pi
        x = r*np.cos(theta)
        y = r*np.sin(theta)

        x_next = r*np.cos(theta_next)
        y_next = r*np.sin(theta_next)

        side_verts = [0,0,h/2],[x,y,-h/2],[x_next,y_next,-h/2]
        faces.append(side_verts)
        bottom_verts.append([x,y,-h/2])

    faces.append(bottom_verts[::-1])

    for face in faces:
        plot_face(ax,face)

    return faces

def bipyramid(ax,h,r,num_of_side):
    """
    will plot a bipyramid with number of sides /2
    """
    faces = []
    plot_axis(ax,max_lim=1.1*max(h,r))
    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi
        theta_next = (2*(n+1)/num_of_side)*np.pi
        x = r*np.cos(theta)
        y = r*np.sin(theta)

        x_next = r*np.cos(theta_next)
        y_next = r*np.sin(theta_next)

        side_verts_top = [0,0,h/2],[x,y,0],[x_next,y_next,0]
        faces.append(side_verts_top)

        side_verts_bottom = [x_next,y_next,0],[x,y,0],[0,0,-h/2]
        faces.append(side_verts_bottom)

    for face in faces:
        plot_face(ax,face)

    return faces

def biprismid(ax,h,dh,r,num_of_side):
    """
    will plot a bi-prism-id with number of sides /2
    """
    faces = []
    plot_axis(ax,max_lim=1.1*max(h,r))
    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi
        theta_next = (2*(n+1)/num_of_side)*np.pi
        x = r*np.cos(theta)
        y = r*np.sin(theta)

        x_next = r*np.cos(theta_next)
        y_next = r*np.sin(theta_next)

        side_verts_top = [0,0,h/2+dh],[x,y,h/2],[x_next,y_next,h/2]
        faces.append(side_verts_top)

        side_verts_mid = [x,y,-h/2],[x_next,y_next,-h/2],[x_next,y_next,h/2],[x,y,h/2]
        faces.append(side_verts_mid)

        side_verts_bottom = [x_next,y_next,-h/2],[x,y,-h/2],[0,0,-h/2-dh]
        faces.append(side_verts_bottom)

    for face in faces:
        plot_face(ax,face)

    return faces