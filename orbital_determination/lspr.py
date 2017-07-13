from numpy import *
from centroid import *

#solves 3 equations with 3 unknowns using Cramer's Rule
def cramer(eq1,eq2,eq3):
    dMat = array([[eq1[0],eq1[1],eq1[2]],
                  [eq2[0],eq2[1],eq2[2]],
                  [eq3[0],eq3[1],eq3[2]]])
    dXMat = array([[eq1[3],eq1[1],eq1[2]],
                  [eq2[3],eq2[1],eq2[2]],
                  [eq3[3],eq3[1],eq3[2]]])
    dYMat = array([[eq1[0],eq1[3],eq1[2]],
                  [eq2[0],eq2[3],eq2[2]],
                  [eq3[0],eq3[3],eq3[2]]])
    dZMat = array([[eq1[0],eq1[1],eq1[3]],
                  [eq2[0],eq2[1],eq2[3]],
                  [eq3[0],eq3[1],eq3[3]]])

    #finds the determinant of D
    dTemp1 = (eq2[1]*eq3[2]-eq2[2]*eq3[1])
    dTemp2 = (eq2[0]*eq3[2]-eq2[2]*eq3[0])
    dTemp3 = (eq2[0]*eq3[1]-eq2[1]*eq3[0])
    d = eq1[0]*dTemp1 - eq1[1]*dTemp2 + eq1[2]*dTemp3

    #finds the determinant of Dx
    dTemp1 = (eq2[1]*eq3[2]-eq2[2]*eq3[1])
    dTemp2 = (eq2[3]*eq3[2]-eq2[2]*eq3[3])
    dTemp3 = (eq2[3]*eq3[1]-eq2[1]*eq3[3])
    dX = eq1[3]*dTemp1 - eq1[1]*dTemp2 + eq1[2]*dTemp3

    #finds the determinant of Dy
    dTemp1 = (eq2[3]*eq3[2]-eq2[2]*eq3[3])
    dTemp2 = (eq2[0]*eq3[2]-eq2[2]*eq3[0])
    dTemp3 = (eq2[0]*eq3[3]-eq2[3]*eq3[0])
    dY = eq1[0]*dTemp1 - eq1[3]*dTemp2 + eq1[2]*dTemp3

    #finds the determinant of Dz
    dTemp1 = (eq2[1]*eq3[3]-eq2[3]*eq3[1])
    dTemp2 = (eq2[0]*eq3[3]-eq2[3]*eq3[0])
    dTemp3 = (eq2[0]*eq3[1]-eq2[1]*eq3[0])
    dZ = eq1[0]*dTemp1 - eq1[1]*dTemp2 + eq1[3]*dTemp3
    
    return [float(dX)/d,float(dY)/d,float(dZ)/d]

def lspr():

    #reads in a file of RA, dec, x, and y coordinates of n known stars
    fileName = raw_input("Enter the file name containing star data: ")
    fitName = raw_input("Enter the fit file name: ")
    data = open(fileName,"r")
    data = data.read()
    data = array(data.split())
    numPoints = len(data)/8
    data.shape = (numPoints,8)
    data = data.astype(float)
    
    xast = input("Enter the x-coordinate of your object: ")
    yast = input("Enter the y-coordinate of your object: ")
    dim = input("Enter the number of points in your regions: ")
    print "Asteroid Centroid and Uncertainty: "
    objCd = centroid(xast,yast,fitName,dim)

    #decimalizes the RA and Dec and separates variables
    ra = []
    for n in data[:,0:3]:
        ra += [n[0] + n[1]/60. + n[2]/3600.]
    dec = []
    for n in data[:,3:6]:
        if n[0] >= 0:
            dec += [n[0] + n[1]/60. + n[2]/3600.]
        else:
            dec += [n[0]- n[1]/60. - n[2]/3600.]

    #calculates specific x and y coordinate of reference stars using centroid
    print "Star Centroids and Uncertainties: "
    starxy = data[:,6:8]
    starCd = []
    for n in starxy:
        tempStar = centroid(n[0],n[1],fitName,dim)
        starCd += [tempStar[0],tempStar[2],tempStar[4]]
    starCd = array(starCd)
    starCd.shape = (numPoints,3)
    
    #finds best-fit plate coefficients
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    xy = 0
    a = 0
    ax = 0
    ay = 0
    d = 0
    dx = 0
    dy = 0

    j = 0
    for i in starCd:
        x += i[0]
        y += i[1]
        x2 += i[0]**2
        y2 += i[1]**2
        xy += i[0]*i[1]
        a += ra[j]
        ax += ra[j]*i[0]
        ay += ra[j]*i[1]
        d += dec[j]
        dx += dec[j]*i[0]
        dy += dec[j]*i[1]
        j += 1
    coeff1 = cramer([numPoints,x,y,a],[x,x2,xy,ax],[y,xy,y2,ay])
    coeff2 = cramer([numPoints,x,y,d],[x,x2,xy,dx],[y,xy,y2,dy])

    coeff = coeff1 + coeff2
    
    #determines residuals and standard deviation of the asteroid
    resa = []
    resd = []
    siga = 0
    sigd = 0
    
    j=0
    for i in starCd:
        resa += [-1*(ra[j] - coeff[0] - coeff[1]*i[0] - coeff[2]*i[1])]
        resd += [-1*(dec[j] - coeff[3] - coeff[4]*i[0] - coeff[5]*i[1])]
        siga += (ra[j] - coeff[0] - coeff[1]*i[0] - coeff[2]*i[1])**2
        sigd += (dec[j] - coeff[3] - coeff[4]*i[0] - coeff[5]*i[1])**2
        j += 1

    siga /= numPoints - 3
    sigd /= numPoints - 3
    sigd = sqrt(sigd)
    siga = sqrt(siga)
    siga *= 3600*15
    sigd *= 3600

    #calculates RA and Dec of the object
    objRA = coeff[0] + coeff[1]*objCd[0] + coeff[2]*objCd[1]
    objDec = coeff[3] + coeff[4]*objCd[0] + coeff[5]*objCd[2]

    print "Star Residuals for RA(s): "
    for n in resa:
        #unit change
        print n*3600*15
    print "Star Residuals for Dec(sec of time): "
    for n in resd:
        #unit change
        print n*3600
    objRAhr = int(objRA)
    objRAmin = int((objRA - objRAhr)*60)
    objRAsec = ((objRA - objRAhr)*60-objRAmin)*60
    objDechr = int(objDec)
    objDecmin = int((objDec - objDechr)*60)
    objDecsec = ((objDec - objDechr)*60-objDecmin)*60
    print "Object RA: " + str(objRAhr), str(objRAmin), str(objRAsec)
    print "Object Dec: " + str(objDechr), str(objDecmin), str(objDecsec)
    print "Asteroid Standard Deviation (RA/DEC): " + str(siga) + "/" + str(sigd)

    #creates a visualization of reference stars and asteroid from data input
    asteroid = sphere(pos=(10*objCd[0],10*objCd[2],0),radius=0.05*siga*sigd,color=color.red)
    for n in starCd:
        star = sphere(pos=(10*n[0],10*n[1],0),radius=n[2]*0.00005,color=color.yellow)
        star.pos -= (10*xast,10*yast,0)
    asteroid.pos -= (10*xast,10*yast,0)
