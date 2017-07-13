# Takes in line parameters and writes it into points.txt
def line():
    m = input("Enter a slope: ")
    b = input("Enter an intercept: ")
    n = input("Enter the number of points: ")
    outFile = open("points.txt", "w")

    x=0
    y=b
    i = 0
    while i < n:
        outFile.write("(" + str(x) + "," + str(y) + ")" + chr(13))
        x += 1
        y += m
        i += 1
    outFile.close()

    

