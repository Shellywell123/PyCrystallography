import numpy as np

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
    will plot a cuboid of given height, width and depth in x,y, and z
    """

    plot_axis(ax,max_lim=1.1*max(h,w,d))
    for i in [-h/2,h/2]:
        for j in [-w/2,w/2]:
            for k in [-d/2,d/2]:
                ax.plot([-i,i],[j,j],[k,k],c='k')
                ax.plot([i,i],[-j,j],[k,k],c='k')
                ax.plot([i,i],[j,j],[-k,k],c='k')

def tetrakis(ax,h,dh):
    """
    will plot a tetrakis
    """
    plot_axis(ax,max_lim=h)
    for i in [-1,1]:
        for j in [-1,1]:
            for k in [-1,1]:
                ax.plot([-i*h/2,i*h/2],[j*h/2,j*h/2],[k*h/2,k*h/2],c='k')
                ax.plot([i*h/2,i*h/2],[-j*h/2,j*h/2],[k*h/2,k*h/2],c='k')
                ax.plot([i*h/2,i*h/2],[j*h/2,j*h/2],[-k*h/2,k*h/2],c='k')


                ax.plot([i*h/2,i*(h/2+dh)] ,[j*h/2,0],[k*h/2,0],c='k')
                ax.plot([i*h/2,0] ,[j*h/2,j*(h/2+dh)],[k*h/2,0],c='k')
                ax.plot([i*h/2,0] ,[j*h/2,0],[k*h/2,k*(h/2+dh)],c='k')

def pyramid(ax,h,num_of_side):
    """
    will plot a pyramid with num of sides -1
    """
    plot_axis(ax,max_lim=1.1*h)

    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi
        theta_next = (2*(n+1)/num_of_side)*np.pi
        x = h*np.cos(theta)
        y = h*np.sin(theta)

        x_next = h*np.cos(theta_next)
        y_next = h*np.sin(theta_next)

        ax.plot([0,x] ,[0,y],[h/2,-h/2],c='k')
        ax.plot([x,x_next] ,[y,y_next],[-h/2,-h/2],c='k')

def bipyramid(ax,h,num_of_side):
    """
    will plot a bipyramid with number of sides /2
    """
    plot_axis(ax,max_lim=1.1*h)
    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi
        theta_next = (2*(n+1)/num_of_side)*np.pi
        x = h*np.cos(theta)
        y = h*np.sin(theta)

        x_next = h*np.cos(theta_next)
        y_next = h*np.sin(theta_next)

        ax.plot([0,x] ,[0,y],[h/2,0],c='k')
        ax.plot([x,x_next] ,[y,y_next],[0,0],c='k')
        ax.plot([0,x] ,[0,y],[-h/2,0],c='k')

def prism(ax,h,num_of_side):
    """
    will plot a prism with number of sides /2
    """
    plot_axis(ax,max_lim=1.1*h)
    for n in range(0,num_of_side):
        theta      = (2*n/num_of_side)*np.pi
        theta_next = (2*(n+1)/num_of_side)*np.pi
        x = h*np.cos(theta)
        y = h*np.sin(theta)

        x_next = h*np.cos(theta_next)
        y_next = h*np.sin(theta_next)

        ax.plot([x,x] ,[y,y],[h/2,-h/2],c='k')
        ax.plot([x,x_next] ,[y,y_next],[h/2,h/2],c='k')
        ax.plot([x,x_next] ,[y,y_next],[-h/2,-h/2],c='k')