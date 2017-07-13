from numpy import *

def det2x2(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]

def det3x3(a):
    return a[0][0]*det2x2(a[1:,1:]) + a[0][2]*det2x2(a[1:,:2]) - a[0][1]*det2x2(a[1:,0:3:2])

def cramers(a,b):
    matX = a.copy()
    matX[:,0] = b.transpose()

    matY = a.copy()
    matY[:,1] = b.transpose()

    matZ = a.copy()
    matZ[:,2] = b.transpose()

    d = det3x3(a)

    return [det3x3(matX)/d,det3x3(matY)/d,det3x3(matZ)/d]
    
