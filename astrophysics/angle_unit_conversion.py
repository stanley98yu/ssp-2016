from math import *

def angleConversion():
    
    #converts the degrees, minutes, and seconds of an angle to only degrees
    degrees = input("Enter the degrees: ")
    minutes = input("Enter the minutes: ")
    seconds = input("Enter the seconds: ")
    
    #If the angle is negative, the values inputted for minutes and seconds
    #must be subtracted. This checks the minus sign convention.
    if degrees < 0:
        angle = degrees - (minutes/60.0) - (seconds/3600.0)
        print angle
    else:
        angle = degrees + (minutes/60.0) + (seconds/3600.0)
        print angle

    rad = input("Convert to radians (0 for no, 1 for yes)? ")
    #converts an angle given in decimal degrees to radians
    if rad == 1:
        angle *= (pi/180)
        print angle

    norm = input("Normalize the angle (0 for no, 1 for yes)? ")
    #normalizes the angle, returning an angle between 0 and 360 degrees
    if norm == 1:
        #checks whether the angle is in radians or degrees
        if rad == 1:
            #keeps subtracting/adding by 2pi until angle is normalized.
            while angle > 2*pi or angle < 0:
                if angle > 2*pi:
                    angle -= 2*pi
                else:
                    angle += 2*pi
            print angle
        else:
            #keeps subtracting/adding by 360 until angle is normalized.
            while angle > 360 or angle < 0:
                if angle > 360:
                    angle -= 360
                else:
                    angle += 360
            print angle
                    
    
