
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
def BCC(ax):
```
```py
def FCC(ax):
```
<p float="left">
  <img src="../Images/BCC.gif" width="400" />
  <img src="../Images/FCC.gif" width="400" />
</p>

```py
def NaCl(ax):
```
```py
def Diamond(ax):
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

