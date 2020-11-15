
# Atomic Structures

## Lattices

```py
prim = primitive_cell_2d('square')
make_lattice(prim)
plt.show()
```

```py
prim = primitive_cell_2d('rhombus')
make_lattice(prim)
plt.show()
```

<p float="left">
  <img src="../Images/square_lattice.gif" width="400" />
  <img src="../Images/rhombus_lattice.gif" width="400" />
</p>

### unit cells

```py
fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
from PyCrystallography import Diamond
prim = Diamond(ax)

fig = plt.figure(1,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
make_lattice_3d(ax,prim)
plt.show()
```
<p float="left">
  <img src="../Images/diamond_unit_cell.gif" width="400" />
  <img src="../Images/diamond_lattice.gif" width="400" />
</p>

```py
fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
from PyCrystallography import Diamond
prim = Diamond(ax)

fig = plt.figure(1,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
make_lattice_3d(ax,prim)
plt.show()
```
<p float="left">
  <img src="../Images/BCC_unit_cell.gif" width="400" />
  <img src="../Images/BCC_latttice.gif" width="400" />
</p>

```py
fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
from PyCrystallography import Diamond
prim = Diamond(ax)

fig = plt.figure(1,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
make_lattice_3d(ax,prim)
plt.show()
```

<p float="left">
  <img src="../Images/NaCl_unit_cell.gif" width="400" />
  <img src="../Images/NaCl_lattice.gif" width="400" />
</p>

```py
fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
from PyCrystallography import Diamond
prim = Diamond(ax)

fig = plt.figure(1,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
make_lattice_3d(ax,prim)
plt.show()
```
<p float="left">
  <img src="../Images/NaCl.gif" width="400" />
  <img src="../Images/diamond.gif" width="400" />
</p>

# Packings

## subdivision

```py
triangle_subdivision(n,'diag')
```

```py
triangle_subdivision(n,'grid')
```

<p float="left">
  <img src="../Images/triangle_subdivision_diag.gif" width="400" />
  <img src="../Images/triangle_subdivision_grid.gif" width="400" />
</p>

```py
triangle_subdivision(n,'zelda')
```

<p float="left">
  <img src="../Images/triangle_subdivision_zelda.gif" width="400" />
</p>

## Penrose Tiling

```py
Penrose_Tiling(n,'sun')
```

```py
Penrose_Tiling(n,'star')
```

<p float="left">
  <img src="../Images/penrose_tiling_sun.gif" width="400" />
  <img src="../Images/penrose_tiling_star.gif" width="400" />
</p>

