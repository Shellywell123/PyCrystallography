# Identifying object symmetries

There are 32 point group classifications for symmetries in crystallography. They are classified by:
 - mirror planes
 - rotational axes (nfold)
 - rotoinversion axes

## n-fold roational symmetry

```py
fig = plt.figure(0,figsize=[8,8])
ax = fig.add_subplot(111,projection='3d')
faces=shape(ax,shapearguments)
points=normal_points(ax,faces,5)
northern_points,southern_points=Stereographic_projection(points,3,'test')
identify_fold_symmetry(northern_points,southern_points)
```

<p float="left">
  <img src="../Images/face_normals_biprismid.gif" width="400" />
  <img src="../Images/stereographic_projection_biprismid.png" width="400" />
</p>

```bash
NFOLD =  5
```

## Miller Indicies

<p float="left">
  <img src="../Images/miller_100.gif" width="400" />
  <img src="../Images/miller_010.gif" width="400" />
  <img src="../Images/miller_001.gif" width="400" />
  <img src="../Images/miller_110.gif" width="400" />
  <img src="../Images/miller_101.gif" width="400" />
  <img src="../Images/miller_011.gif" width="400" />
  <img src="../Images/miller_111.gif" width="400" />
</p>