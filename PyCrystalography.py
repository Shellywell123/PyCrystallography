import numpy as np

################################################################################
# begining of class
################################################################################

class PyGrapher():
    def __init__(self):
       """
       class initaliser
       """
       pass
       
    ######################################################################################

    def plot_plane(self,angle):
        """
        degrees to radians angle converter
        """
        pass

################################################################################
# End of class
################################################################################

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

################################################################################
# begining of class
################################################################################

class PyTransforms():
    def __init__(self):
       """
       class initaliser
       """
       pass

    ######################################################################################

    def degrees_to_radians(self,angle):
        """
        degrees to radians angle converter
        """
        angle = float(angle/180)*np.pi
        return angle

    ######################################################################################

    def x_clockwise(self,x,y,z,theta):
        """
        """
        theta = self.degrees_to_radians(theta)

        X =  x
        Y = -z*np.sin(theta)+y*np.cos(theta)
        Z =  z*np.cos(theta)+y*np.sin(theta)

        return X,Y,Z

    ######################################################################################

    def y_clockwise(self,x,y,z,theta):
        """
        heelflip
        """
        theta = self.degrees_to_radians(theta)

        X =  x*np.cos(theta)+z*np.sin(theta)
        Y =  y
        Z = -x*np.sin(theta)+z*np.cos(theta)

        return X,Y,Z

    ######################################################################################

    def z_clockwise(self,x,y,z,theta):
        """
        bs shuv
        """
        theta = self.degrees_to_radians(theta)

        X =  x*np.cos(theta)+y*np.sin(theta)
        Y = -x*np.sin(theta)+y*np.cos(theta)
        Z =  z

        return X,Y,Z

    ######################################################################################

    def x_anticlockwise(self,x,y,z,theta):
        """
        """
        X,Y,Z = self.x_clockwise(x,y,z,-theta)

        return X,Y,Z

    ######################################################################################

    def y_anticlockwise(self,x,y,z,theta):
        """
        kickflip
        """
        X,Y,Z = self.y_clockwise(x,y,z,-theta)

        return X,Y,Z

    ######################################################################################

    def z_anticlockwise(self,x,y,z,theta):
        """
        fs shuv
        """
        X,Y,Z = self.z_clockwise(x,y,z,-theta)

        return X,Y,Z

    ######################################################################################

    def custom(self,x,y,z,theta_x,theta_y,theta_z):
        """
        for multi dimensional rotations i.e tre flips
        """

        x,y,z = self.x_clockwise(x,y,z,theta_x)
        x,y,z = self.y_clockwise(x,y,z,theta_y)
        x,y,z = self.z_clockwise(x,y,z,theta_z)

        return x,y,z

################################################################################
# End of class
################################################################################
