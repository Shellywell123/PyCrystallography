### Xray-Diffraction
currently work in progress

```py
from PyCrystallography.xray_diffraction import run_simulation

# angle from x axis (degrees)
theta = 60

# number of particles being fired
# - can not be zero, min = 1
num_of_particles = 3

# x distance incomving particles are distribued across
# - can not be zero, min = 1
spread = 1

run_simulation(num_of_particles,theta,spread,lattice_shape='rhombus')
```
<p float="middle">
  <img src="../PyCrystallography/Images/Xray-Diffraction.png" width="400" />
  <img src="../PyCrystallography/Images/Xray-Diffraction2.png" width="400" />
</p>
