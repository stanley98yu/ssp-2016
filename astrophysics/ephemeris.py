from visual import *
from numpy import *
from astro_time import *

#RA AND DEC ARE SLIGHTLY OFF
#takes classical orbital elements and the position of the earth in JD to
#determine the RA and Dec of the asteroid 
def ephemeris():
    #asks user to input classical orbital elements
    a = input("Enter the semi-major axis: ")
    e = input("Enter the eccentricity: ")
    i = input("Enter the inclination: ")
    O = input("Enter the longitude of the ascending node: ")
    w = input("Enter the argument of perihelion: ")
    T = input("Enter the time of perihelion: ")
    tDate = input("Enter the time of observation[yr,mon,day,min,sec]: ")

    #converts to AU, JD, and radians and creates constants
    a /= 1.495978707e8
    i = radians(i)
    O = radians(O)
    w = radians(w)
    t = julian(tDate[0],tDate[1],tDate[2],tDate[3],tDate[4])

    #calculates the mean anomaly(M)
    n = 360/(365*a**1.5)
    M = radians(n*(t-T))
    print "Mean Anomaly(M)= " + str(degrees(M)) + " degrees"

    #calculates the eccentric anomaly(E) using Newton's method
    Ei = 0
    E = M
    while abs(Ei - E) >= 1e-10:
        Ei = E
        E = E - (M - E + e*sin(E))/(-1+e*cos(E))
    print "Eccentric Anomaly(E)= " + str(degrees(E)) + " degrees"

    #calculates the Cartesian coordinates of the asteroid's r and rdot vectors
    r = [a*cos(E)-a*e,a*sqrt(1-e**2)*sin(E),0]
    #rd = [-sin(E),sqrt(1-e**2)*cos(E),0]
    #rd = [rd[0]*((n*a)/(1-e*cos(E))),rd[1]*((n*a)/(1-e*cos(E))),0]
    r = [r[0]*1.495978707e11,r[1]*1.495978707e11,r[2]*1.495978707e11]
    #rd = [rd[0]*1.495978707e11,rd[1]*1.495978707e11,rd[2]*1.495978707e11]
    print "r(orbit)= " + str(r)
    #print "rdot(orbit)= " + str(rd)
    
    #rotates orbital position vector to ecliptic coordinates(3 transformations)
    r = [r[0]*cos(w)-r[1]*sin(w),r[0]*sin(w)+r[1]*cos(w),r[2]]
    r = [r[0],r[1]*cos(i)-r[2]*sin(i),r[1]*sin(i)+r[2]*cos(i)]
    r = [r[0]*cos(O)-r[1]*sin(O),r[0]*sin(O)+r[1]*cos(O),r[2]]
    #rd = [rd[0]*cos(w)-rd[1]*sin(w),rd[0]*sin(w)+rd[1]*cos(w),rd[2]]
    #rd = [rd[0],rd[1]*cos(i)-rd[2]*sin(i),rd[1]*sin(i)+rd[2]*cos(i)]
    #rd = [rd[0]*cos(O)-rd[1]*sin(O),rd[0]*sin(O)+rd[1]*cos(O),rd[2]]

    #rotates the position vector from ecliptic to equatorial coordinates
    eps = radians(23.4)
    r = [r[0],r[1]*cos(eps)-r[2]*sin(eps),r[1]*sin(eps)+r[2]*cos(eps)]
    #rd = [rd[0],rd[1]*cos(eps)-rd[2]*sin(eps),rd[1]*sin(eps)+rd[2]*cos(eps)]
    print "r(equatorial)= " + str(r)
    #print "rdot(equatorial)= " + str(rd)
    r = [r[0]/(1.495978707e11),r[1]/(1.495978707e11),r[2]/(1.495978707e11)]

    #finds the earth-sun vector(R) through JPL Horizons
    R = [-.3813504426077191,.8650197321619791,.3753258432756818]
    print "R= " + str(R)

    #calculates the range vector(rho) from r and R
    rho = [r[0]+R[0],r[1]+R[1],r[2]+R[2]]
    rho = [rho[0]*1.495978707e11,rho[1]*1.495978707e11,rho[2]*1.495978707e11]
    print "RhoVector= " + str(rho)

    #calculates the RA and Dec
    dec = asin(rho[2]/mag(rho))
    cosRA = (rho[0]/mag(rho))/cos(dec)
    sinRA = (rho[1]/mag(rho))/cos(dec)
    ra = atan2(sinRA,cosRA)
    if ra < 0:
        ra += 2*pi
    ra *= (24/(2*pi))
    ramin = (ra-int(ra))*60
    rasec = (ramin-int(ramin))*60
    dec = degrees(dec)
    decdg = int(dec)
    decmin = (dec-decdg)*60
    decsec = (decmin-int(decmin))*60
    print "RA(Geocentric)=", str(int(ra)), str(int(ramin)), str(int(rasec))
    print "Dec(Geocentric)=", str(decdg), str(int(decmin)), str(int(decsec))

    #determines RA and Dec based on LST
    LST = 12 + 28./60 + 57.8419/3600 #found through JPL Horizons at Boulder
    LST *= (2*pi)/24
    lat = radians(40.0150) #currently at Boulder
    rE = 6.371/1.495978707e11
    dD = [rE*cos(lat)*cos(LST),rE*cos(lat)*sin(LST),rE*sin(lat)]
    rhot = [rho[0]-dD[0],rho[1]-dD[1],rho[2]-dD[2]]
    
    dec = asin(rhot[2]/mag(rhot))
    cosRA = (rhot[0]/mag(rhot))/cos(dec)
    sinRA = (rhot[1]/mag(rhot))/cos(dec)
    ra = atan2(sinRA,cosRA)
    if ra < 0:
        ra += 2*pi
    ra *= (24/(2*pi))
    ramin = (ra-int(ra))*60
    rasec = (ramin-int(ramin))*60
    dec = degrees(dec)
    decdg = int(dec)
    decmin = (dec-decdg)*60
    decsec = (decmin-int(decmin))*60
    print "RA(Topocentric)=", str(int(ra)), str(int(ramin)), str(int(rasec))
    print "Dec(Topocentric)=", str(decdg), str(int(decmin)), str(int(decsec))
