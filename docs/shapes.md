
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
  <img src="../Images/cube.gif" width="400" />
  <img src="../Images/cuboid_x.gif" width="400" />
  <img src="../Images/cuboid_y.gif" width="400" />
  <img src="../Images/cuboid_z.gif" width="400" />
</p>

### Pyramids
```py
def pryamid(ax,h,num_of_side):
```
<p float="left">
  <img src="../Images/pyramid3.gif" width="400" />
  <img src="../Images/pyramid4.gif" width="400" />
  <img src="../Images/pyramid5.gif" width="400" />
  <img src="../Images/pyramid10.gif" width="400" />
</p>

### Bipyramids
```py
def bipryamid(ax,h,num_of_side):
```
<p float="left">
  <img src="../Images/bipyramid3.gif" width="400" />
  <img src="../Images/bipyramid4.gif" width="400" />
  <img src="../Images/bipyramid5.gif" width="400" />
  <img src="../Images/bipyramid10.gif" width="400" />
</p>

### Prisms
```py
def prism(ax,h,num_of_side):
```
<p float="left">
  <img src="../Images/prism3.gif" width="400" />
  <img src="../Images/prism4.gif" width="400" />
  <img src="../Images/prism5.gif" width="400" />
  <img src="../Images/prism10.gif" width="400" />
</p>

### Biprismid (not sure what its proper name is)
```py
def biprismid(ax,h,num_of_side):
```
<p float="left">
  <img src="../Images/biprismid3.gif" width="400" />
  <img src="../Images/biprismid4.gif" width="400" />
  <img src="../Images/biprismid5.gif" width="400" />
  <img src="../Images/biprismid10.gif" width="400" />
</p>

### Tetrakis
```py
def tetrakis(ax,h,dh):
```
<p float="left">
  <img src="../Images/tetrakis.gif" width="400" />
</p>