
# Atomic Structures of crystals

## Miller Indices

The miller indices are used to denote the planes in crstallography in a crystal lattice.

<p float="left">
  <img src="../Images/miller_100.gif" width="400" />
  <img src="../Images/miller_010.gif" width="400" />
  <img src="../Images/miller_001.gif" width="400" />
  <img src="../Images/miller_110.gif" width="400" />
  <img src="../Images/miller_101.gif" width="400" />
  <img src="../Images/miller_011.gif" width="400" />
  <img src="../Images/miller_111.gif" width="400" />
</p>


## Planes of reflections in a Cube
```py

def cube_reflection(ax):
```
```py

def cube_reflection_diag(ax):
```
<p float="left">
  <img src="../Images/cube_reflection.gif" width="400" />
  <img src="../Images/cube_reflection_diag.gif" width="400" />
</p>

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
prim = BCC(ax)

fig = plt.figure(1,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
make_lattice_3d(ax,prim)
plt.show()
```
<p float="left">
  <img src="../Images/BCC_unit_cell.gif" width="400" />
  <img src="../Images/BCC_lattice.gif" width="400" />
</p>

```py
fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
prim = FCC(ax)

fig = plt.figure(1,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
make_lattice_3d(ax,prim)
plt.show()
```

<p float="left">
  <img src="../Images/FCC_unit_cell.gif" width="400" />
  <img src="../Images/FCC_lattice.gif" width="400" />
</p>

```py
fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d',azim=30,elev=30)
prim = NaCl(ax)

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

