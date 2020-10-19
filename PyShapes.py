def cuboid(ax,h,w,d):
    """
    """
    for i in [-h/2,h/2]:
        for j in [-w/2,w/2]:
            for k in [-d/2,d/2]:
                ax.plot([-i,i],[j,j],[k,k],c='k')
                ax.plot([i,i],[-j,j],[k,k],c='k')
                ax.plot([i,i],[j,j],[-k,k],c='k')