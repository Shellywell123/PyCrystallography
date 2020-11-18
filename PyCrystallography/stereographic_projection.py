import numpy as np

#########################################
# symmetry
#########################################

def identify_fold_symmetry(n_points,e_points,s_points):
    """
    going to be a function that check the circle of which a point lies  on stereo proj  on to count all other points on that circle and return that as th en fold symm
    if only one point.
    """
    nfold_results = []
    for points in [n_points,e_points,s_points]:
        if points == n_points:
            print('\nN-hemi {} points'.format(len(points)))
        else:
            print('\nS-hemi {} points'.format(len(points)))
        print('radius,theta_sum,theta,mean,checkval')

        polar_coords = []
        
        for point in points:

            # get points radial coord
            # count how many other points lie on a circle of the same radius
            # gruop points by radial dist and check the al have same n fold (igrore points at origin)
            # return count
         #   print(point)
            x = point[0]
            y = point[1]
            r = np.sqrt(x**2 + y**2)
            theta = np.arctan(y/x)
          #  if theta == -0.0:
           #     theta = np.pi
            if theta < 0 :
                theta = 2*np.pi+theta
            if np.isnan(theta) == True:
                theta = 0.0
            polar_coords.append([r,theta])

        #leave 0 in list as it can be folded any way
        checked_rs = [0]

        #generate list of radii
        list_of_r = []
        for point in polar_coords:
            list_of_r.append(point[0])

        polar_coords_copy = polar_coords

        # search for raddii indexs and use that to check angles of set radial dists
        for i in range(0,len(polar_coords_copy)):
            current_r = polar_coords[i][0]
            if current_r not in checked_rs:
               # print(current_r)
                searchval = current_r
             #   print(list_of_r)
                indexs = np.where(list_of_r == searchval)[0]
                checked_rs.append(current_r)

                #current method for checking nfold is 
                # that the mean angle should = 2pi/nfold, for nfold num of points
                theta_sum = 0
                for index in indexs:
                    current_theta = polar_coords[index][1]
               #     print(current_r,current_theta)
                    theta_sum = theta_sum + current_theta

                theta_mean = theta_sum/len(indexs)    

                if theta_mean > np.pi:
                    theta_mean = 2*(theta_mean-np.pi)           

               # print(current_r,theta_sum,theta_mean,2*np.pi/len(indexs),len(indexs))

                if theta_mean == 2*np.pi/len(indexs):
                 #   print(indexs)
                    result =len(indexs)
                    nfold_results.append(result)
            else:
                pass

        if all(element == nfold_results[0] for element in nfold_results):
            print('NFOLD = ',nfold_results[0])
