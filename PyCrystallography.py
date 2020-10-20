from PyShapes import plot_axis
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
    