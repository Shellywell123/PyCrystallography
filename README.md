# PyCrystallography

Python 3 package being written to illustrate crystallography.\\
\\
The features of the package include:
 - [Atomic Structures](https://github.com/Shellywell123/PyCrystallography/blob/main/docs/atomic_structures.md)
 - [Crystal Models](https://github.com/Shellywell123/PyCrystallography/blob/main/docs/shapes.md)
 - [Stereographic Projections](https://github.com/Shellywell123/PyCrystallography/blob/main/docs/stereographic_projections.md)
 - [Operations](https://github.com/Shellywell123/PyCrystallography/blob/main/docs/operations.md)
 - [Stereographic Projections](https://github.com/Shellywell123/PyCrystallography/blob/main/docs/stereographic_projections.md)
 - [symmetries](https://github.com/Shellywell123/PyCrystallography/blob/main/docs/idenitfying_symmetries.md)

## Penrose Tiling

```py
Penrose_Tiling(n,'sun')
```

```py
Penrose_Tiling(n,'star')
```

<p float="left">
  <img src="Images/penrose_tiling_sun.gif" width="400" />
  <img src="Images/penrose_tiling_star.gif" width="400" />
</p>

## Atomic Structures
More info at [Atomic Structures](https://github.com/Shellywell123/PyCrystallography/blob/main/docs/atomic_structures.md)

```py
def BCC(ax):
```
```py
def FCC(ax):
```
<p float="left">
  <img src="Images/BCC_unit_cell.gif" width="400" />
  <img src="Images/FCC_unit_cell.gif" width="400" />
</p>

```py
def NaCl(ax):
```
```py
def Diamond(ax):
```
<p float="left">
  <img src="Images/NaCl_unit_cell.gif" width="400" />
  <img src="Images/diamond_unit_cell.gif" width="400" />
</p>


## Operations
More info at [Operations](https://github.com/Shellywell123/PyCrystallography/blob/main/docs/operations.md)

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

def cube_reflection(ax):
```
```py

def cube_reflection_diag(ax):
```
<p float="left">
  <img src="Images/cube_reflection.gif" width="400" />
  <img src="Images/cube_reflection_diag.gif" width="400" />
</p>

## Face normal detection and Stereographic Projections
More info at [Stereographic Projections](https://github.com/Shellywell123/PyCrystallography/blob/main/docs/stereographic_projections.md)

<p float="left">
  <img src="Images/face_normals_tetrakis.gif" width="400" />
  <img src="Images/stereographic_projection_tetrakis.png" width="400" />
</p>


## Shapes
More info at [Shapes](https://github.com/Shellywell123/PyCrystallography/blob/main/docs/shapes.md)

<p float="left">
  <img src="Images/cube.gif" width="400" />
  <img src="Images/pyramid5.gif" width="400" />
  <img src="Images/bipyramid10.gif" width="400" />
  <img src="Images/prism5.gif" width="400" />
  <img src="Images/prism10.gif" width="400" />
  <img src="Images/biprismid5.gif" width="400" />
  <img src="Images/biprismid10.gif" width="400" />
  <img src="Images/tetrakis.gif" width="400" />
</p>

## Identifying Symmetries
More info at [symmetries](https://github.com/Shellywell123/PyCrystallography/blob/main/docs/idenitfying_symmetries.md)
