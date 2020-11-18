
#########################################
# operations
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