# PyCrystallography

## Atomic Structures
<p float="left">
  <img src="Images/BCC.gif" width="400" />
  <img src="Images/FCC.gif" width="400" />
  <img src="Images/NaCl.gif" width="400" />
</p>


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
### Cuboids
<p float="left">
  <img src="Images/cube.gif" width="400" />
  <img src="Images/cuboid.gif" width="400" />
  <img src="Images/cuboid1.gif" width="400" />
  <img src="Images/cuboid2.gif" width="400" />
</p>

### Pyramids
<p float="left">
  <img src="Images/triangular_pyramid.gif" width="400" />
  <img src="Images/square_pyramid.gif" width="400" />
  <img src="Images/pentagon_pyramid.gif" width="400" />
  <img src="Images/decagon_pyramid.gif" width="400" />
</p>

### Spintops
<p float="left">
  <img src="Images/spintop3.gif" width="400" />
  <img src="Images/spintop4.gif" width="400" />
  <img src="Images/spintop5.gif" width="400" />
  <img src="Images/spintop10.gif" width="400" />
</p>
