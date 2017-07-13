from visual import *
from numpy import *
from vectors import *
from lspr import *

#read vector orbital elements and outputs the classical orbital elements
def orbElem(fileName):
    #reads a text file containing the r and rdot vectors and puts it in an array
    data = open(fileName,"r")
    data = data.read()
    data = array(data.split())
    data.shape = (2,3)
    data = data.astype(float)
    print data

    #calculates the semi-major axis
    r0 = mag(data[0])
    v02 = mag(data[1])**2
    a = 1./((2/r0)-v02)
    print "a: " + str(a) + " AU"

    #calculates the eccentricity
    h = cross(data[0],data[1])
    e = sqrt(1-((mag(h)**2)/a))
    print "e: " + str(e)

    #calculates inclination
    i = atan2(sqrt(h[0]**2+h[1]**2),h[2])
    print "i: " + str(degrees(i))

    #calculates the longitude of the ascending node
    cosO = -h[1]/(mag(h)*sin(i))
    sinO = h[0]/(mag(h)*sin(i))
    omegaL = atan2(sinO,cosO)
    print "Omega: " + str(degrees(omegaL))

    #calculates the argument of perihelion
    cosU = (data[0][0]*cos(omegaL) + data[0][1]*sin(omegaL))/r0
    sinU = data[0][2]/(r0*sin(i))
    U = atan2(sinU,cosU)
    if U < 0:
        U += 2*pi
    cosV = ((a*(1-e**2)/r0)-1)/e
    sinV = (a*(1-e**2)/(e*mag(h)))*(dot(data[0],data[1])/r0)
    v = atan2(sinV,cosV)
    if v < 0:
        v += 2*pi
    omegaS = U - v
    if omegaS < 0:
        omegaS += 2*pi
    print "omega: " + str(degrees(omegaS))

    #creates a 3D visualization of the orbit:
    #creates the orbital plane and the shape of the orbit
    orbital = box(pos=(0,0,0), length=10, height=.1, width=10,
                   color=color.white)
    t = arange(0,2*pi+.001,.001)
    orbit = curve(x=a*cos(t)-a*e,z=sqrt(a**2-(a*e)**2)*sin(t), 
                  radius=.1, color=color.black)

    #creates the ecliptic plane
    ecliptic = box(pos=(0,0,0), length = 10, height=.1, width=10, axis=data[0],
                   color=color.yellow)

    #creates the three orientation vectors: h, e, and N
    hVector = arrow(pos=(0,0,0), axis=(0,3*mag(h),0), color=color.magenta)
    NVector = arrow(pos=(0,0,0), axis=(3*cos(omegaL),0,3*data[0][2]),
                    color=color.cyan)
    eVector = arrow(pos=(0,0,0), axis=(-7*cos(omegaL-pi/2),0,7*sin(omegaL)),
                    color=color.green)
    
    
