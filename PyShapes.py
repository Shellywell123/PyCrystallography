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
        current_r = np.sqrt(normal[0]**2 + normal[1]**2 + normal[2]**2)

        normal = normal * r/current_r

        sphere_points.append(normal)
        ax.plot([face_centre[0],normal[0]],[face_centre[1],normal[1]],[face_centre[2],normal[2]],linewidth=3,c='k')
        ax.scatter(normal[0],normal[1],normal[2],linewidth=3,c='k')

    return sphere_points

def plot_face(ax,verts):
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
    ax.add_collection3d(Poly3DCollection(verts,linewidths=1,edgecolor='k',alpha=0.5))

def cuboid(ax,h,w,d):
    """
    """
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
        plot_face(ax,face)

    return faces


def prism(ax,h_z,r_xy,num_of_side):
    """
    will plot a prism of given height, width and depth in x,y, and z
    """
    h = h_z

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

        side_verts = [x,y,h/2],[x_next,y_next,h/2],[x_next,y_next,-h/2],[x,y,-h/2]
        faces.append(side_verts)

        top_verts.append([x,y,h/2])
        bottom_verts.append([x,y,-h/2])

    faces.append(top_verts)
    faces.append(bottom_verts)

    for face in faces:
        plot_face(ax,face)

    return faces



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
    faces = []
    bottom_verts = []
    plot_axis(ax,max_lim=1.1*h)

    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi
        theta_next = (2*(n+1)/num_of_side)*np.pi
        x = h*np.cos(theta)
        y = h*np.sin(theta)

        x_next = h*np.cos(theta_next)
        y_next = h*np.sin(theta_next)

        side_verts = [0,0,h/2],[x,y,-h/2],[x_next,y_next,-h/2]
        faces.append(side_verts)
        bottom_verts.append([x,y,-h/2])

    faces.append(bottom_verts[::-1])

    for face in faces:
        plot_face(ax,face)

    return faces

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

# def prism(ax,h,num_of_side):
#     """
#     will plot a prism with number of sides /2
#     """
#     bonds =[]
#     plot_axis(ax,max_lim=1.1*h)
#     for n in range(0,num_of_side):
#         theta      = (2*n/num_of_side)*np.pi
#         theta_next = (2*(n+1)/num_of_side)*np.pi
#         x = h*np.cos(theta)
#         y = h*np.sin(theta)

#         x_next = h*np.cos(theta_next)
#         y_next = h*np.sin(theta_next)

#         bonds.append(make_bond([x,x] ,[y,y],[h/2,-h/2],1,'k'))
#         bonds.append(make_bond([x,x_next] ,[y,y_next],[h/2,h/2],1,'k'))
#         bonds.append(make_bond([x,x_next] ,[y,y_next],[-h/2,-h/2],1,'k'))
#     plot_bonds(ax,bonds)

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