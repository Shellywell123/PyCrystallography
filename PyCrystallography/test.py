import matplotlib.pyplot as plt
fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d')
from PyCrystallography import geometry
geometry.cuboid(ax,2,2,2)
plt.show()