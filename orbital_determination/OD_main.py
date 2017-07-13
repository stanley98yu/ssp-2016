from math import *
from numpy import *
from lspr import cramer
from vectors import *

#determines the orbit of the asteroid by finding the vector orbital elements
#of the middle observation time using Gauss' method, and determines classical
#orbital elements
def od(fileName):
    #reads in data from a text file (time, RA, Dec, Rx, Ry, Rz)
    data = open(fileName,"r")
    data = data.read()
    data = array(data.split())
    data.shape = (3,6)
    data = data.astype(float)

    #separates data into individual lists for clarity and convenience
    #R[AU],t[JD],ra[hr],dec[deg] 
    time = data[:,0]
    ra = data[:,1]
    dec = data[:,2]
    earthSun = data[:,3:6]

    #converts RA and Dec into radians for use in Python
    i = 0
    while i < 3:
        ra[i] *= 15
        ra[i] = radians(ra[i])
        dec[i] = radians(dec[i])
        i += 1

    #finds the rho-hat vectors for all three observations
    rhoH1 = [cos(ra[0])*cos(dec[0]),sin(ra[0])*cos(dec[0]),sin(dec[0])]
    rhoH2 = [cos(ra[1])*cos(dec[1]),sin(ra[1])*cos(dec[1]),sin(dec[1])]
    rhoH3 = [cos(ra[2])*cos(dec[2]),sin(ra[2])*cos(dec[2]),sin(dec[2])]

    #finds the values of tau (time intervals)
    k = 0.01720209895
    tn1 = k*(time[0]-time[1])
    t0 = k*(time[2]-time[0])
    t1 = k*(time[2]-time[1])
    
    #finds the values of the a coefficients
    a1 = t1/t0
    a3 = -tn1/t0

    #finds the magnitudes of the rho vector
    med1 = a1*earthSun[0][0]-earthSun[1][0]+a3*earthSun[2][0]
    med2 = a1*earthSun[0][1]-earthSun[1][1]+a3*earthSun[2][1]
    med3 = a1*earthSun[0][2]-earthSun[1][2]+a3*earthSun[2][2]
    rho = cramer([a1*rhoH1[0],-rhoH2[0],a3*rhoH3[0],med1],
                 [a1*rhoH1[1],-rhoH2[1],a3*rhoH3[1],med2],
                 [a1*rhoH1[2],-rhoH2[2],a3*rhoH3[2],med3])

    #performs light travel time correction
    c = 173.1446
    tn1c = time[0]-time[1] - rho[0]/c
    t0c = time[2]-time[0] - rho[1]/c
    t1c = time[2]-time[1] - rho[2]/c
    tn1c *= k
    t0c *= k
    t1c *= k

    #calculates the vector orbital elements r and rdot at middle observation
    #r[AU],rdot[AU/GD]
    rhon1 = [rho[0]*rhoH1[0],rho[0]*rhoH1[1],rho[0]*rhoH1[2]]
    rho0 = [rho[1]*rhoH2[0],rho[1]*rhoH2[1],rho[1]*rhoH2[2]]
    rho1 = [rho[2]*rhoH3[0],rho[2]*rhoH3[1],rho[2]*rhoH3[2]]
    i = 0
    r = []
    rn1 = []
    r1 = []
    while i < 3:
        r += [rho0[i]-earthSun[1][i]]
        rn1 += [rhon1[i]-earthSun[0][i]]
        r1 += [rho1[i]-earthSun[2][i]]
        i += 1
    i = 0
    rdot = []
    while i < 3:
        rdot += [(r1[i]-rn1[i])/t0]
        i += 1

    #performs linear interpolation
    #i = 0
    #v12 = []
    #v23 = []
    #while i < 3:
        #v12 += [(r[i]-rn1[i])/(t0-tn1)]
        #v23 += [(r1[i]-r[i])/(t1-t0)]
        #rdot[i] = ((t1-t0)*v12[i] + (t0-tn1)*v23[i])/(t1-tn1)
        #i += 1
    

    #computes the f-series and g-series (Taylor Series)
    fMinus = 1-(tn1**2)/(2*(mag(r))**3)+(dot(r,rdot)*tn1**3)/(2*mag(r)**5)
    fPlus = 1-(t1**2)/(2*(mag(r))**3)+(dot(r,rdot)*t1**3)/(2*mag(r)**5)
    gMinus = tn1-((tn1**3)/(6*(mag(r))**3))
    gPlus = t1-((t1**3)/(6*(mag(r))**3))
    aM = gPlus/(fMinus*gPlus-fPlus*gMinus)
    aP = -gMinus/(fMinus*gPlus-fPlus*gMinus)
    i = 0
    while i < 3:
        r[i] = (gPlus*rn1[i]-gMinus*r1[i])/(fMinus*gPlus-fPlus*gMinus)
        rdot[i] = (fPlus*rn1[i]-fMinus*r1[i])/(fPlus*gMinus-fMinus*gPlus)
        i += 1
    
    #computes new r and rdot vectors by iteration
    count = 1
    testX = 1
    testY = 1
    testZ = 1
    rOld = [0,0,0]
    rdotOld = [0,0,0]
    while testX >= 1e-9 or testY >= 1e-9 or testZ >= 1e-9:
        #begins new iteration by setting the iterative vectors to previous ones
        i = 0
        while i < 3:
            rOld[i] = r[i]
            rdotOld[i] = rdot[i]
            i += 1
        
        #calculates the rho components with formulas
        med1 = aM*earthSun[0][0]-earthSun[1][0]+aP*earthSun[2][0]
        med2 = aM*earthSun[0][1]-earthSun[1][1]+aP*earthSun[2][1]
        med3 = aM*earthSun[0][2]-earthSun[1][2]+aP*earthSun[2][2]
        rho = cramer([aM*rhoH1[0],-rhoH2[0],aP*rhoH3[0],med1],
                 [aM*rhoH1[1],-rhoH2[1],aP*rhoH3[1],med2],
                 [aM*rhoH1[2],-rhoH2[2],aP*rhoH3[2],med3])

        #performs light travel time correction
        c = 173.1446
        tn1c = time[0]-time[1] - rho[0]/c
        t0c = time[2]-time[0] - rho[1]/c
        t1c = time[2]-time[1] - rho[2]/c
        tn1c *= k
        t0c *= k
        t1c *= k
        
        #calculates new vector iterative orbital elements r and rdot
        i = 0
        while i < 3:
            rn1[i] = rho[0]*rhoH1[i] - earthSun[0][i]
            r1[i] = rho[2]*rhoH3[i] - earthSun[2][i]
            r[i] = (gPlus*rn1[i]-gMinus*r1[i])/(fMinus*gPlus-fPlus*gMinus)
            rdot[i] = (fPlus*rn1[i]-fMinus*r1[i])/(fPlus*gMinus-fMinus*gPlus)
            i += 1

        #performs linear interpolation
        #i = 0
        #v12 = []
        #v23 = []
        #while i < 3:
            #v12 += [(r[i]-rn1[i])/(t0-tn1)]
            #v23 += [(r1[i]-r[i])/(t1-t0)]
            #rdot[i] = ((t1-t0)*v12[i] + (t0-tn1)*v23[i])/(t1-tn1)
            #i += 1
        
        #calculates refined f-series and g-series, then calculates refined "a"
        fMinus = 1-(tn1**2)/(2*mag(r)**3)+(dot(r,rdot)*tn1**3)/(2*mag(r)**5)
        fPlus = 1-(t1**2)/(2*mag(r)**3)+(dot(r,rdot)*t1**3)/(2*(mag(r)**5))
        gMinus = tn1-(tn1**3)/(6*(mag(r)**3))
        gPlus = t1-(t1**3)/(6*(mag(r)**3))
        aM = gPlus/(fMinus*gPlus-fPlus*gMinus)
        aP = -gMinus/(fMinus*gPlus-fPlus*gMinus)
    
        testX = abs(r[0] - rOld[0])
        testY = abs(r[1] - rOld[1])
        testZ = abs(r[2] - rOld[2])
        count += 1
    print str(count) + " iterations"
    print "r: " + str(r)
    print "rdot: " + str(rdot)

    #rotates equatorial r and rdot to ecliptic
    eps = radians(23.5)
    r = [r[0],r[2]*sin(eps)+r[1]*cos(eps),-r[1]*sin(eps)+r[2]*cos(eps)]
    rdot = [rdot[0],rdot[2]*sin(eps)+rdot[1]*cos(eps),-rdot[1]*sin(eps)+rdot[2]*cos(eps)]
    print "r rotated: " + str(r)
    print "rdot rotated: " + str(rdot)

    #calculates the classical orbital elements using r and rdot
    data = array([r,rdot])
    data.shape = (2,3)
    
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
    if omegaL < 0:
        omegaL += 2*pi
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

    #calculates the mean anomaly
    E = atan2((((1-e**2)**.5)*sin(v)),(e+cos(v)))
    M = E - e*sin(E)
    print "M: " + str(degrees(M))
            
