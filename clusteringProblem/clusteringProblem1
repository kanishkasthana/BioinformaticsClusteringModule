#Script Written by Kanishk Asthana to do clustering using numpy arrays and python classes

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import random
from clusteringProblem.points import *
import scipy.spatial.distance as dst


outputFile=open("output.txt", 'w')
inputFile=open("dataset_10926_14.txt",'r')
input=inputFile.read().splitlines()
firstLineInputs=input[0].split()

#Getting Values of K and M for the clustering problem
k=int(firstLineInputs[0])
m=int(firstLineInputs[1])

#Getting an array of all the points
pointVector=list(map(point,input[1:]))

#Choosing Random point to Start clustering algorithm
randomPoint=center(pointVector[0])

print(randomPoint.coordinate)

#Defining a list to Store Centers for clusters
centers=[randomPoint]

while centers.__len__()<k:
    #Getting nearest center to point
    for point in pointVector:
        point.getNearestCenter(centers)
    pointWithMaximumDistanceToCenters=max(pointVector,key=lambda point:point.distanceToNearestCenter)
    #Creating new center object as the point that maximizes the distance to center and adding it to the centers list
    centers.append(center(pointWithMaximumDistanceToCenters))

#Writing output for grading from Stepic
for c in centers:
    outputFile.write(" ".join(map(str,c.coordinate))+"\n")


inputFile.close()
outputFile.close()