from math import *

#takes the sine and cosine of an angle and returns the angle in radians
def angle(s,c):
    return atan2(s,c)

#takes the values of two sides and the included angle of a spherical triangle
#in radians and returns the other side and angle in radians
def sphTriRad(a,b,cI):
    c = acos(cos(a)*cos(b) + sin(a)*sin(b)*cos(cI))
    aI = asin((sin(cI)/sin(c))*sin(a))
    bI = asin((sin(cI)/sin(c))*sin(b))

    return [c,aI,bI]

#takes the values of two sides and the included angle of a spherical triangle
#in degrees and returns the other side and angle in degrees
def sphTriDeg():
    a = input("Enter one side in decimal degrees: ")
    b = input("Enter another side in decimal degrees: ")
    cI = input("Enter the included angle in decimal degrees: ")

    a = radians(a)
    b = radians(b)
    cI = radians(cI)

    #uses Law of Sine and Law of Cosine to find the answers in degrees
    c = acos(cos(a)*cos(b) + sin(a)*sin(b)*cos(cI))
    aI = degrees(asin((sin(cI)/sin(c))*sin(a)))
    bI = degrees(asin((sin(cI)/sin(c))*sin(b)))
    c = degrees(c)

    return [c,aI,bI]
