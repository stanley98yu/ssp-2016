from math import *

def toRadians(degrees): #converts degrees to radians
    return degrees * pi / 180

def roots(a,b,c): #computes the roots of a given quadratic polynomial
    disc = b*b - 4*a*c
    if disc > 0:
        x1 = (-b + sqrt(disc))/(2*a)
        x2 = (-b - sqrt(disc))/(2*a)
        return [x1,x2]
    if disc == 0:
        return -b / (2*a)
    else:
        return []
    
def eligibility(age,cit): #determines eligibility for House and Senate
    #US Senators must be at least 30 years old and a US citizen for at least
    #9 years. US Representatives must be at least 25 years old and a US
    #citizen for 7 years.
    if age >= 30 and cit >= 9:
        return "You are eligibile for both the House and Senate."
    elif age >= 25 and cit >= 7:
        return "You are eligibile only for the House."
    else:
        return "You are ineligible for Congress."
    
def prime(x): #determines if x is a prime number
    for i in range(2,x): #checks every number between 1 and x
        if x%i == 0:
            return "Your number is not prime."
    return "Your number is prime."
