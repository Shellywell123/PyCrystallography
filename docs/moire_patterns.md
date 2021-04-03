# Moire patterns

moire pattens can be seen by translating/rotating an indetical lattice/structure over the top of itself.

```py
from PyCrystallography.moire import linear_rot_pattern
# n being a angle in degrees
linear_rot_pattern(n)
```

```py
from PyCrystallography.moire import grid_rot_pattern
# n being a angle in degrees
grid_rot_pattern(n)
```

```py
from PyCrystallography.moire import radial_seperation_pattern
# d being the seperation
radial_seperation_pattern(d)
```

<p float="middle">
  <img src="../PyCrystallography/Images/moire_pattern_linear_roatation.gif" style="width: 25vw;" />
  <img src="../PyCrystallography/Images/moire_pattern_radial_seperation.gif" style="width: 25vw;" />
  <img src="../PyCrystallography/Images/moire_grid_rotation.gif" style="width: 25vw;" />
</p>

