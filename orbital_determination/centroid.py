from visual import *
from numpy import *
import pyfits

#calculates the centroid for the specific data set given
def testCentroid():
    #calculates centroid
    r1 = 33 + 21 + 33 + 8
    r2 = 56 + 51 + 53 + 26
    r4 = 55 + 101 + 116 + 50 + 16
    r5 = 11 + 78 + 26 + 2 + 10
    c1 = 23 + 55 + 11
    c2 = 33 + 56 + 120 + 101 + 78
    c4 = 33 + 53 + 73 + 50 + 2
    c5 = 8 + 26 + 18 + 16 + 10
    sum = r1 + r2 + r4 + r5 + 23 + 120 + 149 + 73 + 18
    xcm = (c1*-2 + c2*-1 + c4*1 + c5*2)/float(sum)
    ycm = (r1*2 + r2*1 + r4*-1 + r5*-2)/float(sum)
    
    #calculates uncertainty. I used the formula for the uncertainty of the
    #center of mass and input the position value subtracted by the
    #centroid value all divided by the total quantity squared. After
    #multiplying each by n, I took the suare root to compute the final answer.
    xsq = c1*(-2-xcm)**2 + c2*(-1-xcm)**2 + c4*(1-xcm)**2 + c5*(2-xcm)**2
    ysq = r1*(2-ycm)**2 + r2*(1-ycm)**2 + r4*(-1-ycm)**2 + r5*(-2-ycm)**2
    xunc = (xsq/(sum**2))**.5
    yunc = (ysq/(sum**2))**.5
    return [str(xcm) + " +/- " + str(xunc),str(ycm) + " +/- " + str(yunc)]

#reads in a set of data elements from a text file and outputs the centroid.
def centroidTextFile():
    #allows the user to input a file to read and dimensions of data
    fileName = raw_input("Enter the file name: ")
    dim = sqrt(input("Enter the number of points: "))
    data = open(fileName,"r")

    #reads data from file, converts it into an array, then translates into float
    data = data.read()
    data = array(data.split())
    data.shape = (dim,dim)
    data = data.astype(float)
    print data

    xcenter = input("Enter x-coordinate of origin(0 for default): ")
    ycenter = input("Enter y-coordinate of origin(0 for default): ")

    if xcenter != 0 and ycenter != 0:
        tempData = data[ycenter-1:ycenter+2,xcenter-1:xcenter+2]
        data = tempData
        dim = 3
    print data
    
    ydata = data.copy()
    xdata = data.copy().transpose()

    #calculates sum
    sum = 0
    for r in data:
        for c in r:
            sum += c

    #gets the row/column values to calculate the centroid
    i = 0
    j = int(dim)/2
    ycm = 0
    xcm = 0 
    while i < dim:
        yrow = 0
        xrow = 0
        for n in ydata[i]:
            yrow += n
        for n in xdata[i]:
            xrow += n
        yrow *= j
        xrow *= -j
        ycm += yrow
        xcm += xrow
        j -= 1
        i += 1

    ycm /= sum
    xcm /= sum

    #gets the row/column values to get the uncertainty
    i = 0
    j = int(dim)/2
    ysq = 0
    xsq = 0 
    while i < dim:
        yrow = 0
        xrow = 0
        for n in ydata[i]:
            yrow += n
        for n in xdata[i]:
            xrow += n
        ysq += yrow*(j-ycm)**2
        xsq += xrow*(-j-xcm)**2
        j -= 1
        i += 1

    yunc = (ysq/(sum**2))**.5
    xunc = (xsq/(sum**2))**.5
    
    print "Centroid:", [xcm,ycm]
    print "Uncertainty:", [xunc,yunc]

#reads in a set of pixel values from a data file and outputs the centroid
def centroid(xcenter,ycenter,fileName,dim):
    #allows the user to input a file to read and dimensions of data
    image = pyfits.getdata(fileName)

    #presents data opened, and asks for origin and number of points
    n = image.shape[0]
    dim = sqrt(dim)

    #finds center of desired area and prepares data
    edge = int(dim)/2
    ycenter -= 1
    xcenter -= 1
    data = image[ycenter-edge:ycenter+edge+1,xcenter-edge:xcenter+edge+1]

    ydata = data.copy()
    xdata = data.copy().transpose()

    #calculates sum
    sum = 0
    for r in data:
        for c in r:
            sum += c

    #gets the row/column values to calculate the centroid
    i = 0
    j = int(dim)/2
    ycm = 0
    xcm = 0 
    while i < dim:
        yrow = 0
        xrow = 0
        for n in ydata[i]:
            yrow += n
        for n in xdata[i]:
            xrow += n
        yrow *= j
        xrow *= -j
        ycm += yrow
        xcm += xrow
        j -= 1
        i += 1

    ycm /= sum
    xcm /= sum
    xcm += xcenter
    ycm += ycenter

    #gets the row/column values to get the uncertainty
    i = 0
    j = int(dim)/2
    ysq = 0
    xsq = 0 
    while i < dim:
        yrow = 0
        xrow = 0
        for n in ydata[i]:
            yrow += n
        for n in xdata[i]:
            xrow += n
        ysq += yrow*(j-ycm)**2
        xsq += xrow*(-j-xcm)**2
        j -= 1
        i += 1

    yunc = (ysq/(sum**2))**.5
    xunc = (xsq/(sum**2))**.5
    
    print "Centroid:", [xcm,ycm]
    print "Uncertainty:", [xunc,yunc]
 
    return [xcm,xunc,ycm,yunc,sum]

    #creates a visualization of the centroid relative to the original input
    #y = 0
    #x = 0
    #while x < dim:
        #while y < dim:
            #ball = sphere(pos=(x*3,y*3,0), radius = data[x][y]*0.000005, color = color.yellow)
            #y += 1
        #x += 1
        #y = 0
    #cball = sphere(pos=((xcm+int(dim)/2)*3,(ycm+int(dim)/2)*3,0), radius = 0.000005*sum/(dim**2), color = color.red)
