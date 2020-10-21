from PyShapes import plot_axis
def BCC(ax):
    """
    plot the body centered cubic primitive cell
    """

    h =2
    w =2
    d =2
    plot_axis(ax,max_lim=3)
    for i in [-h/2,h/2]:
        for j in [-w/2,w/2]:
            for k in [-d/2,d/2]:
                ax.plot([-i,i],[j,j],[k,k],c='k',alpha=0.5)
                ax.plot([i,i],[-j,j],[k,k],c='k',alpha=0.5)
                ax.plot([i,i],[j,j],[-k,k],c='k',alpha=0.5)

                COL ='red'
                SIZ =50

                ax.scatter([i,i],[j,j],[k,k],c=COL,s=SIZ)

def FCC(ax):
    """
    plots the face centred cubic primitive cell
    """

    h =2
    w =2
    d =2
    plot_axis(ax,max_lim=3)
    for i in [-h/2,h/2]:
        for j in [-w/2,w/2]:
            for k in [-d/2,d/2]:
                ax.plot([-i,i],[j,j],[k,k],c='k',alpha=0.5)
                ax.plot([i,i],[-j,j],[k,k],c='k',alpha=0.5)
                ax.plot([i,i],[j,j],[-k,k],c='k',alpha=0.5)

                COL ='red'
                SIZ =50

                ax.scatter([i,i],[j,j],[k,k],c=COL,s=SIZ)
                ax.scatter([0,0],[0,0],[k,k],c=COL,s=SIZ)
                ax.scatter([0,0],[j,j],[0,0],c=COL,s=SIZ)
                ax.scatter([i,i],[0,0],[0,0],c=COL,s=SIZ)
def NaCl(ax):
    """
    plots the nacl atom structure
    """

    h =2
    w =2
    d =2
    plot_axis(ax,max_lim=3)
    for i in [-h/2,0,h/2]:
        for j in [-w/2,0,w/2]:
            for k in [-d/2,0,d/2]:
                ax.plot([-i,i],[j,j],[k,k],c='k',alpha=0.5)
                ax.plot([i,i],[-j,j],[k,k],c='k',alpha=0.5)
                ax.plot([i,i],[j,j],[-k,k],c='k',alpha=0.5)

                if (abs(i)==abs(j)==abs(k)!=0)or(abs(i)+abs(j)+abs(k)==h/2):
                    COL ='green'
                    SIZ =50
                else:
                    COL = 'red'
                    SIZ = 20

                ax.scatter([i,i],[j,j],[k,k],c=COL,s=SIZ)
    
def Diamond(ax):
    """
    plots the diamond atom structure
    """
    h =2
    w =2
    d =2
    plot_axis(ax,max_lim=2)
    for i in [-h/2,h/2]:
        for j in [-w/2,w/2]:
            for k in [-d/2,d/2]:
                # ax.plot([-i,i],[j,j],[k,k],c='k',alpha=0.5)
                # ax.plot([i,i],[-j,j],[k,k],c='k',alpha=0.5)
                # ax.plot([i,i],[j,j],[-k,k],c='k',alpha=0.5)

                COL ='red'
                SIZ =50
                if i+j+k==h/2:
                    ax.scatter([i,i],[j,j],[k,k],c=COL,s=SIZ)
                ax.scatter([0,0],[0,0],[k,k],c=COL,s=SIZ)
                ax.scatter([0,0],[j,j],[0,0],c=COL,s=SIZ)
                ax.scatter([i,i],[0,0],[0,0],c=COL,s=SIZ)

    ax.scatter([-h/2],[-h/2],[-h/2],c=COL,s=SIZ)

    ax.scatter([-h/4],[-h/4],[-h/4],c=COL,s=SIZ)
    ax.scatter([h/4],[h/4],[-h/4],c=COL,s=SIZ)
    ax.scatter([-h/4],[h/4],[h/4],c=COL,s=SIZ)
    ax.scatter([h/4],[-h/4],[h/4],c=COL,s=SIZ)

    ax.plot([-h/2,-h/4],[-h/2,-h/4],[-h/2,-h/4],c='k')
    ax.plot([h/2,h/4],[h/2,h/4],[-h/2,-h/4],c='k')

    ax.plot([-h/2,-h/4],[h/2,h/4],[h/2,h/4],c='k')
    ax.plot([h/2,h/4],[-h/2,-h/4],[h/2,h/4],c='k')

    ax.plot([-h/2,-h/4],[0,h/4],[0,h/4],c='k')
    ax.plot([h/2,h/4],[0,-h/4],[0,h/4],c='k')

    ax.plot([0,-h/4],[-h/2,-h/4],[0,-h/4],c='k')
    ax.plot([0,-h/4],[h/2,h/4],[0,h/4],c='k')

    ax.plot([-h/2,-h/4],[0,-h/4],[0,-h/4],c='k')
    ax.plot([h/2,h/4],[0,h/4],[0,-h/4],c='k')

    ax.plot([0,h/4],[-h/2,-h/4],[0,h/4],c='k')
    ax.plot([0,h/4],[h/2,h/4],[0,-h/4],c='k')

    ax.plot([-h/4,0],[-h/4,0],[-h/4,-h/2],c='k')
    ax.plot([-h/4,0],[h/4,0],[h/4,h/2],c='k')

    ax.plot([h/4,0],[h/4,0],[-h/4,-h/2],c='k')
    ax.plot([h/4,0],[-h/4,0],[h/4,h/2],c='k')

def inversion(ax,h,w,d):
    """
    plots an annotated points being inversed through the orgin
    """
    plot_axis(ax)
    #cube(ax,7,7,7)

    pos = 1
    ax.plot([-h,h],[-w,w],[-d,d],c='k',linestyle='--')
    ax.text(h+pos,w+pos,d+pos,r"$(x,y,z)$")
    ax.text(-h-pos,-w-pos,-d-pos,r"$-(x,y,z)$")

def reflection(ax,h,w,d):
    """
    plots a annotated point being mirrored in a plotted plane
    """
    plot_axis(ax)

    pos = 1
    ax.plot([h,h],[w,w],[-d,d],c='k',linestyle='--')
    ax.text(h+pos,w+pos,d+pos,r"$(x,y,z)$")
    ax.text(h-pos,w-pos,-d-pos,r"$-(x,y,z)$")

    h = h+3
    w= w+3
    plane(ax,h,w,d,plane_axis='z')

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
    plot_axis(ax)
    pass

def cube_reflection(ax,h,w,d):
    """
    cube with some internal refelctive planes plotted
    """
    plot_axis(ax)
    from PyShapes import cuboid
    cuboid(ax,h,w,d)
    h=h/2
    w=w/2
    d=d/2
    plane(ax,h,w,d,'x')
    plane(ax,h,w,d,'y')
    plane(ax,h,w,d,'z')

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

def Stereographic_projection(ax):
    """
    takes x,y,z coords that all lie on the surface of a 
    sphere and outputs a 2d stereograph
    """
    x,y,z,r =test_sphere(ax)

    x_ = []
    y_ = []

    import numpy as np

    import matplotlib.pyplot as plt

  

    plt.figure()

    for i in range(0,len(x)):
        x_.append(x[i]/(1-z[i]))
        y_.append(y[i]/(1-z[i]))

        if z[i] > 0:
            plt.scatter(x_[i],y_[i],marker='2',label='N',c='k',s=50)
        else:
            plt.scatter(x_[i],y_[i],marker='1',label='S',c='k',s=50)

    theta = np.linspace(0,2*np.pi,100)
    xc = (r+1)*np.cos(theta)
    yc = (r+1)*np.sin(theta)
    plt.legend(loc=1)
    plt.plot(xc,yc,alpha=0.5,c='k')
    plt.axis('off')
    plt.savefig('stereographic_projection_cube.png')
    plt.show()
