from math import *

#takes in hour angle and declination and returns altitude and azimuth at SBO
def toAltAzi(ha,dec):
    #converts values to radians
    lat = radians(40.015)
    dec = radians(dec)
    ha = radians(ha)

    #uses the Law of Cosine to determine altitude
    c = cos(pi/2-lat)*cos(pi/2-dec) + sin(pi/2-lat)*sin(pi/2-dec)*cos(ha)
    alt = 90 - degrees(acos(c))

    #uses the Law of Cosine to determine azimuth
    c1 = cos(pi/2-dec) - cos(pi/2-lat)*cos(radians(90-alt))
    c2 = c1/(sin(pi/2-lat)*sin(radians(90-alt)))
    if ha < pi:
        azi = 360 - degrees(acos(c2))
    else:
        azi = degrees(acos(c2))
    return [alt,azi]

#takes equatorial coordinates and returns ecliptic coordinates
def ecliptic(ra, dec):
    #converts values tor radians
    ra = radians(ra)
    dec = radians(dec)
    ecl = 23.5 * (pi/180)

    #rotates the coordinates along the ecliptic plane using rotation matrix
    decEcl = asin(-sin(ra)*cos(dec)*sin(ecl) + sin(dec)*cos(ecl))
    raEcl = atan2((sin(ra)*cos(dec)*cos(ecl) + sin(dec)*sin(ecl)),(cos(ra)*cos(dec)))

    #accounts for the negative values of arctan
    while raEcl < 0:
        raEcl += 2*pi
        
    return [degrees(raEcl),degrees(decEcl)]

#converts date and time to Julian Date
def julian(year,month,day,hour,min):

    #formula for converting to JD
    a = (14-month)/12
    y = year + 4800 - a
    m = month + 12*a -3

    jdn = day + (153*m+2)/5 + 365*y + y/4 - y/100 + y/400 - 32045

    return jdn + (hour-12)/24. + min/1440.

