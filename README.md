# PyCrystallography

## Inversion Reflection Rotation
<p float="left">
  <img src="Images/inversion.gif" width="290" />
  <img src="Images/reflection.gif" width="290" />
  <img src="Images/rotation.gif" width="290" />
</p>


```py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PyShapes import *
```
```py
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
plot_axis(ax)
cuboid(ax,5,5,5)

plt.show()
```
<p float="left">
  <img src="Images/cube.gif" width="400" />
  <img src="Images/cuboid.gif" width="400" />
  <img src="Images/cuboid2.gif" width="400" />
</p>

