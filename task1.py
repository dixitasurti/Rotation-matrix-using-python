###############
##Design the function "findRotMat" to  return 
# 1) rotMat1: a 2D numpy array which indicates the rotation matrix from xyz to XYZ 
# 2) rotMat2: a 2D numpy array which indicates the rotation matrix from XYZ to xyz 
#It is ok to add other functions if you need
###############

import numpy as np
import cv2

def findRotMat(alpha, beta, gamma):

    angle = np.radians(alpha)
    cosz,sinz = np.cos(angle),np.sin(angle)
    rZi = [(cosz,-sinz,0),(sinz,cosz,0),(0,0,1)]
    angle = np.radians(beta)
    cosx,sinx = np.cos(angle),np.sin(angle)
    rXii = [(1,0,0),(0,cosx,-sinx),(0,sinx,cosx)]
    angle = np.radians(gamma)
    cosz,sinz = np.cos(angle),np.sin(angle)
    rZ = [(cosz,-sinz,0),(sinz,cosz,0),(0,0,1)]
    rXrY = np.dot(rZ,rXii)
    rXrYrZ = np.dot(rXrY,rZi)
    #rotational matrices are orthogonal
    # sub question 2
    rXrYrZ_inverse = rXrYrZ.T
    return rXrYrZ,rXrYrZ_inverse


if __name__ == "__main__":
    alpha = 45
    beta = 30
    gamma = 60
    rotMat1, rotMat2 = findRotMat(alpha, beta, gamma)
    print(rotMat1)
    print(rotMat2)
