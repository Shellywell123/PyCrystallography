# PyCrystallography

## Atomic Structures
```py
def BCC(ax):
```
```py
def FCC(ax):
```
<p float="left">
  <img src="Images/BCC.gif" width="400" />
  <img src="Images/FCC.gif" width="400" />
</p>

```py
def NaCl(ax):
```
```py
def Diamond(ax):
```
<p float="left">
  <img src="Images/NaCl.gif" width="400" />
  <img src="Images/diamond.gif" width="400" />
</p>


## Inversion & Reflection
```py
def inversion(ax,h,w,d):
```
```py
def reflection(ax,h,w,d):
```
<p float="left">
  <img src="Images/inversion.gif" width="400" />
  <img src="Images/reflection.gif" width="400" />
</p>


### Reflective Planes
```py

def cube_reflection(ax,h,w,d):
```
<p float="left">
  <img src="Images/cube_reflection.gif" width="400" />
</p>

## Face normal detection and Stereographic Projection
```py

fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d')
h,w,d = 2,2,5
faces = cuboid(ax,2,2,2)
r = max(h,w,d)
points=normal_points(ax,faces,r)
Stereographic_projection(ax,points,r)
plt.show()
```
<p float="left">
  <img src="Images/face_normals_cube.gif" width="400" />
  <img src="Images/stereographic_projection_cube.png" width="250" />
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
```py
def cuboid(ax,h,w,d):
```
<p float="left">
  <img src="Images/cube.gif" width="400" />
  <img src="Images/cuboid_x.gif" width="400" />
  <img src="Images/cuboid_y.gif" width="400" />
  <img src="Images/cuboid_z.gif" width="400" />
</p>

### Pyramids
```py
def pryamid(ax,h,num_of_side):
```
<p float="left">
  <img src="Images/pyramid3.gif" width="400" />
  <img src="Images/pyramid4.gif" width="400" />
  <img src="Images/pyramid5.gif" width="400" />
  <img src="Images/pyramid10.gif" width="400" />
</p>

### Bipyramids
```py
def bipryamid(ax,h,num_of_side):
```
<p float="left">
  <img src="Images/bipyramid3.gif" width="400" />
  <img src="Images/bipyramid4.gif" width="400" />
  <img src="Images/bipyramid5.gif" width="400" />
  <img src="Images/bipyramid10.gif" width="400" />
</p>

### Prisms
```py
def prism(ax,h,num_of_side):
```
<p float="left">
  <img src="Images/prism3.gif" width="400" />
  <img src="Images/prism4.gif" width="400" />
  <img src="Images/prism5.gif" width="400" />
  <img src="Images/prism10.gif" width="400" />
</p>

### Biprismid (not sure what its proper name is)
```py
def biprismid(ax,h,num_of_side):
```
<p float="left">
  <img src="Images/biprismid3.gif" width="400" />
  <img src="Images/biprismid4.gif" width="400" />
  <img src="Images/biprismid5.gif" width="400" />
  <img src="Images/biprismid10.gif" width="400" />
</p>

### Tetrakis
```py
def tetrakis(ax,h,dh):
```
<p float="left">
  <img src="Images/tetrakis.gif" width="400" />
</p>