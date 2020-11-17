import matplotlib.pyplot as plt
fig = plt.figure(0,figsize=[8,8])
azim = 30
ax = fig.add_subplot(111,projection='3d',azim=azim,elev=30)
from PyCrystallography import reflection
reflection(ax,1,1,1)
plt.show()