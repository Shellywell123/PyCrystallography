# import numpy as np
# r_uc = 0.5

# x_points = []
# y_points = []

# dtheta_uc = 2*np.pi/6
# for i in range(0,6):
#     ang = i*dtheta_uc+dtheta_uc/2
#     x_points.append(r_uc*np.sin(ang)+r_uc)
#     y_points.append(r_uc*np.cos(ang)+r_uc)

# print(x_points,y_points)

# import matplotlib.pyplot as plt 
# plt.plot(x_points,y_points)
# plt.show()

from PyCrystallography import lattice
from PyCrystallography  import unit_cell

uc = unit_cell.primitive_cell_2d('hexagon')
latp=lattice.make_lattice_2d(uc,depth=5)

import matplotlib.pyplot as plt 
plt.scatter(latp[0],latp[1])
plt.show()