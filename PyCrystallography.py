from PyShapes import plot_axis
def BCC(ax):
    """
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