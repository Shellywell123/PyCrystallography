
## Geometry

PyCrystallography contains many 3D geometries that can be loaded and viewed interactively. The models can then have there normals identified and converted to [Stereographic Projections](https://github.com/Shellywell123/PyCrystallography/blob/main/docs/stereographic_projections.md).
```py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PyCrystallography.geometry import *
```
```py
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
######################################
# which ever 3d model you want to load
cuboid(ax,5,5,5)
######################################
plt.show()
```
### Cuboids
```py
def cuboid(ax,h,w,d):
```
<p float="left">
  <img src="../PyCrystallography/Images/cube.gif" width="400" />
  <img src="../PyCrystallography/Images/cuboid_x.gif" width="400" />
  <img src="../PyCrystallography/Images/cuboid_y.gif" width="400" />
  <img src="../PyCrystallography/Images/cuboid_z.gif" width="400" />
</p>

### Pyramids
```py
def pryamid(ax,h,num_of_side):
```
<p float="left">
  <img src="../PyCrystallography/Images/pyramid3.gif" width="400" />
  <img src="../PyCrystallography/Images/pyramid4.gif" width="400" />
  <img src="../PyCrystallography/Images/pyramid5.gif" width="400" />
  <img src="../PyCrystallography/Images/pyramid10.gif" width="400" />
</p>

### Bipyramids
```py
def bipryamid(ax,h,num_of_side):
```
<p float="left">
  <img src="../PyCrystallography/Images/bipyramid3.gif" width="400" />
  <img src="../PyCrystallography/Images/bipyramid4.gif" width="400" />
  <img src="../PyCrystallography/Images/bipyramid5.gif" width="400" />
  <img src="../PyCrystallography/Images/bipyramid10.gif" width="400" />
</p>

### Prisms
```py
def prism(ax,h,num_of_side):
```
<p float="left">
  <img src="../PyCrystallography/Images/prism3.gif" width="400" />
  <img src="../PyCrystallography/Images/prism4.gif" width="400" />
  <img src="../PyCrystallography/Images/prism5.gif" width="400" />
  <img src="../PyCrystallography/Images/prism10.gif" width="400" />
</p>

### Biprismid 
(not sure what its proper name is)
```py
def biprismid(ax,h,num_of_side):
```
<p float="left">
  <img src="../PyCrystallography/Images/biprismid3.gif" width="400" />
  <img src="../PyCrystallography/Images/biprismid4.gif" width="400" />
  <img src="../PyCrystallography/Images/biprismid5.gif" width="400" />
  <img src="../PyCrystallography/Images/biprismid10.gif" width="400" />
</p>

### Tetrakis
```py
def tetrakis(ax,h,dh):
```
<p float="left">
  <img src="../PyCrystallography/Images/tetrakis.gif" width="400" />
</p>
