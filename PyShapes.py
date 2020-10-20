import numpy as np

def plot_axis(ax):
    """
    """
    ax.set_facecolor('white')
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

    ax.grid(False)

    max_lim = 10
    min_lim = -max_lim
    ax.auto_scale_xyz([min_lim, max_lim],
                [min_lim, max_lim], 
                [0, 2*max_lim])   

    #make axes at orgin
    #plt.axes(False)
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
    """

    plot_axis(ax)
    for i in [-h/2,h/2]:
        for j in [-w/2,w/2]:
            for k in [-d/2,d/2]:
                ax.plot([-i,i],[j,j],[k,k],c='k')
                ax.plot([i,i],[-j,j],[k,k],c='k')
                ax.plot([i,i],[j,j],[-k,k],c='k')
    
def pryamid(ax,h,num_of_side):
    """
    """
    plot_axis(ax)

    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi
        theta_next = (2*(n+1)/num_of_side)*np.pi
        x = h*np.cos(theta)
        y = h*np.sin(theta)

        x_next = h*np.cos(theta_next)
        y_next = h*np.sin(theta_next)

        ax.plot([0,x] ,[0,y],[h/2,-h/2],c='k')
        ax.plot([x,x_next] ,[y,y_next],[-h/2,-h/2],c='k')

def inversion(ax,h,w,d):
    """
    """
    plot_axis(ax)
    #cube(ax,7,7,7)

    pos = 1
    ax.plot([-h,h],[-w,w],[-d,d],c='k',linestyle='--')
    ax.text(h+pos,w+pos,d+pos,r"$(x,y,z)$")
    ax.text(-h-pos,-w-pos,-d-pos,r"$-(x,y,z)$")

def reflection(ax,h,w,d):
    """
    """
    plot_axis(ax)
    #cube(ax,7,7,7)

    pos = 1
    ax.plot([h,h],[w,w],[-d,d],c='k',linestyle='--')
    ax.text(h+pos,w+pos,d+pos,r"$(x,y,z)$")
    ax.text(h-pos,w-pos,-d-pos,r"$-(x,y,z)$")

    h = h+3
    w= w+3
    plane(ax,h,w,d,plane_axis='z')

def plane(ax,h,w,d,plane_axis):
    """
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
    plot_axis(ax)
    pass

def cube_reflection(ax,h,w,d):
    """
    """
    plot_axis(ax)
    cuboid(ax,h,w,d)
    h=h/2
    w=w/2
    d=d/2
    plane(ax,h,w,d,'x')
    plane(ax,h,w,d,'y')
    plane(ax,h,w,d,'z')