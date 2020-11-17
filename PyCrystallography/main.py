import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PyShapes import *
from PyCrystallography import *

fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d')
#faces = cuboid(ax,2,2,2)
#reflection(ax,2,2,2)
faces=pyramid(ax,2,2,3)
# faces=biprismid(ax,3,1,0.5,5)
points=normal_points(ax,faces,5)
# print(points)

# ns,es,ss=Stereographic_projection(points,3,'test')
# #print(ns,ss)
# identify_fold_symmetry(ns,es,ss)
plt.show()