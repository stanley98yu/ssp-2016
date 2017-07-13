from visual import *
from visual.graph import *
from random import randint

#creates a random 2D walk
def random2D():
    #creates ball and trail 
    ball = sphere(pos=(0,0,0),radius=0.1)
    ball.trail = curve(color=color.white)
    dt = .01
    while 1:
        #runs through random walks by randomizing an angle and step = 1
        rate(75)
        ang = random.randint(-pi,pi)
        ball.velocity = vector(cos(ang),sin(ang),0)
        ball.pos += ball.velocity*dt
        ball.trail.append(pos=ball.pos)

#creates a random 3D walk
def random3D():
    #creates ball and trail
    ball = sphere(pos=(0,0,0),radius=0.1)
    ball.trail = curve(color=color.white)
    dt = .01
    while 1:
        #runs through random walk (2 angles this time because 3D)
        rate(75)
        ang = random.randint(-pi,pi)
        ang2 = random.randint(-pi,pi)
        ball.velocity = vector(cos(ang)*cos(ang2),cos(ang2)*sin(ang),sin(ang2))
        ball.pos += ball.velocity*dt
        ball.trail.append(pos=ball.pos)
        
#creates a random 1D walk and calculates and graphs displacement
def random1D(N):
    #initializes a ball and display window
    ball = sphere(pos=(0,0,0),radius=0.1)
    ball.trail = curve(color=color.white)
    #gd = gdisplay(width=600,height=600,xmax=100,xmin=-100,ymax=200,ymin=0)
    histo = ghistogram(bins=arange(-100,100,1),color=color.white)
    n = 1
    d = []
    #creates histogram with data
    while 1:
        while n <= N:
            step = random.randint(0,2)
            if step == 0:
                step = -1
            n += 1
            ball.pos += (step,0,0)
        displacement = ball.pos.x
        d += [displacement]
        histo.plot(data=d)
        n = 0
        ball.pos = (0,0,0)
