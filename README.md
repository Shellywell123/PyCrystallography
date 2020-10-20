# PyCrystallography

## Inversion Reflection Rotation
<p float="left">
  <img src="Images/inversion.gif" width="400" />
  <img src="Images/reflection.gif" width="400" />
  <img src="Images/rotation.gif" width="400" />
</p>


## Reflective Planes
<p float="left">
  <img src="Images/cube_reflection.gif" width="400" />
</p>


## Shapes
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
  <img src="Images/cuboid1.gif" width="400" />
  <img src="Images/cuboid2.gif" width="400" />
</p>

<p float="left">
  <img src="Images/triangular_pyramid.gif" width="400" />
  <img src="Images/square_pyramid.gif" width="400" />
  <img src="Images/pentgon_pyramid.gif" width="400" />
  <img src="Images/decagon_pyramid.gif" width="400" />
</p>