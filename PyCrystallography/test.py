import numpy as np
import matplotlib.pyplot as plt

def z_anticlockwise(x,y,theta):
    """
    bs shuv
    """
    theta = -np.radians(theta)

    X =  x*np.cos(theta)+y*np.sin(theta)
    Y = -x*np.sin(theta)+y*np.cos(theta)

    return X,Y


x1=0
x2=100

N =100

x = np.linspace(x1,x2,N)
y = np.sin(x)

for theta in range(0,360):
    x_,y_ = z_anticlockwise(x,y,theta)
    plt.plot(x_,y_)
plt.show()


