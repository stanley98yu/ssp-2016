from numpy import *

#goes through the Fruit Ninja Academy exercises
def fruitNinja():
    fruits = array([["Apple","Banana","Blueberry","Cherry"],
                    ["Coconut","Grapefruit","Kumquat","Mango"],
                    ["Nectarine","Orange","Tangerine","Pomegranate"],
                    ["Lemon","Raspberry","Strawberry","Tomato"]])

    #a. extracts Tomato in one command
    print fruits[3][3]

    #b. extracts the inner 2x2 in one command
    print fruits[1:3,1:3]

    #c. extracts the first and third rows in one command
    print fruits[:3:2,:]

    #d. extracts the inner 2x2 flipped vertically and horizontally
    print fruits[2:0:-1,2:0:-1]

    #e. swaps first and fourth columns in three commands
    fruity = fruits.copy()
    fruity[:,0:4:3] = fruits[:,3::-3]
    print fruity

    #f. replaces everything in the array with "SLICED!"
    fruits[:,:] = ("SLICED!")
    print fruits
