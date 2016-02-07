#Script written by Kanishk Asthana to contain the points class.

import numpy as np
import scipy.spatial.distance as dst

#Defining a class to store all the points for the algorithm
class point:
    def __init__(self,inputString):
        self.coordinate=np.fromstring(inputString,dtype=float,sep=" ")
        self.nearestCenter=None
        self.distanceToNearestCenter=None

    def getNearestCenter(self,centers):
        minCenter=min(centers,key=lambda c: dst.euclidean(c.coordinate,self.coordinate) )
        self.nearestCenter=minCenter
        self.nearestCenter.addPoint(self)
        self.distanceToNearestCenter=dst.euclidean(self.nearestCenter.coordinate,self.coordinate)

#Defining subclass to store the centers
class center(point):
    def __init__(self,point):
        self.coordinate=point.coordinate
        self.nearestCenter=point
        self.points=[]
    def addPoint(self,point):
        self.points.append(point)



