from math import *
import pyfits

#pulls boxes of pixel values of out of an image or fit file
def photometry():
    #allows the user to input a file to read 
    fileName = raw_input("Enter the file name: ")
    image = pyfits.getdata(fileName)
    print image

    #asks the user to input details of the star or asteroid
    n = image.shape[0]
    xStar = input("Enter the x-coordinate of the object: ")
    yStar = input("Enter the y-coordinate of the object: ")
    dim = input("Enter the dimension of the object: ")/2.

    #sums all of the pixels in designated box
    starBox = image[yStar-dim:yStar+dim+1,xStar-dim:xStar+dim+1]
    print starBox
    starBkg = 0
    for a in starBox:
        for b in a:
            starBkg += b
    print "Star + Background = " + str(starBkg)

    #asks the user to input details of a blank portion
    xBkg = input("Enter the x-coordinate of a blank portion: ")
    yBkg = input("Enter the y-coordinate of a blank portion: ")
    #sums all of the pixels in designated blank box
    blankBox = image[yBkg-dim:yBkg+dim+1,xBkg-dim:xBkg+dim+1]
    print blankBox
    bkg = 0
    for a in blankBox:
        for b in a:
            bkg += b
    print "Background = " + str(bkg)

    #calculates pixel count
    count = starBkg - bkg
    print "Pixel count = " + str(count)

    #calculates the constant
    mag = input("Enter the magnitude of the object: ")
    const = mag + 2.5*log10(count)
    print "Constant = " + str(const)

    #asks the user to input details of the asteroid
    xAst = input("Enter the x-coordinate of your asteroidn: ")
    yAst = input("Enter the y-coordinate of your asteroid: ")

    #sums the pixels in the asteroid's designated box
    astBox = image[yAst-dim:yAst+dim+1,xAst-dim:xAst+dim+1]
    print astBox
    ast = 0
    for a in astBox:
        for b in a:
            ast += b
    ast -= bkg
    print "Asteroid = " + str(ast)

    #calculates the magnitude of the asteroid
    print "Magnitude = " + str(-2.5*log10(ast) + const)
