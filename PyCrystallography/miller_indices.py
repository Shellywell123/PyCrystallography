
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

    from PyCrystallography.geometry import cuboid
    cuboid(ax,2,2,2,alpha=0.01,show_axis=False)
    ax.plot([-1, 1],[-1,-1],[-1,-1],c='r',label='V1',linewidth=5)
    ax.plot([-1,-1],[-1, 1],[-1,-1],c='b',label='V2',linewidth=5)
    ax.plot([-1,-1],[-1,-1],[-1, 1],c='g',label='V3',linewidth=5)

    from PyCrystallography.structure import plot_face
    plot_face(ax,verts,color='pink')
    ax.plot([],[],[],c='pink',label=index)

    ax.legend()
    ax.axis('off')

def cube_reflection(ax):
    """
    cube with some internal refelctive planes plotted
    """

    from PyCrystallography.geometry import cuboid
    cuboid(ax,2,2,2,alpha=0.01)

    verts_100 = [[0,-1,-1],[0,1,-1],[0,1,1],[0,-1,1]]
    verts_010 = [[-1,0,-1],[1,0,-1],[1,0,1],[-1,0,1]]
    verts_001 = [[-1,-1,0],[1,-1,0],[1,1,0],[-1,1,0]]

    from PyCrystallography.structure import plot_face
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
    from PyCrystallography.geometry import cuboid
    cuboid(ax,2,2,2,alpha=0.01)

    verts_110 = [[-1,1,1],[1,-1,1],[1,-1,-1],[-1,1,-1]]
    verts_101 = [[-1,-1,1],[-1,1,1],[1,1,-1],[1,-1,-1]]
    verts_011 = [[-1,-1,1],[1,-1,1],[1,1,-1],[-1,1,-1]]

    from PyCrystallography.structure import plot_face
    plot_face(ax,verts_110,color='yellow')
    ax.plot([],[],[],c='yellow',label='<110>')

    plot_face(ax,verts_101,color='orange')
    ax.plot([],[],[],c='orange',label='<010>')

    plot_face(ax,verts_011,color='purple')
    ax.plot([],[],[],c='purple',label='<001>')

    ax.legend()
