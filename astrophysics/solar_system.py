from visual import *

#creates a model of a solar system including the planets through Jupiter
def solarSystem():

    #initializes the display window for the solar system
    solarSystem = display(width=700,height=700,range=5)

    #creates the sun and the planets up to Jupiter
    sun = sphere(pos=(0,0,0),radius=4, mass = 1.99,
                 material=materials.emissive,color=color.yellow)
    earth = sphere(a=14.9,e=.0167,pos=(14.9,0,0),radius=.637,veloc=vector(0,0,0),
                   material=materials.earth)
    mercury = sphere(a=5.79,e=.2056,pos=(5.79,0,0),radius=.244,
                     color=color.blue)
    venus = sphere(a=10.8,e=.0067,pos=(10.8,0,0),radius=.605,
                     color=color.magenta)
    mars = sphere(a=22.8,e=.0935,pos=(22.8,0,0),radius=.339,
                     color=color.red)
    jupiter = sphere(a=77.9,e=.0489,pos=(77.9,0,0),radius=1.49,
                     color=color.green)

#displays the orbit of the celestial body
    t = arange(0,2*pi+.001,.001)
    earthEllipse = curve(x=earth.a*cos(t)-earth.a*earth.e,
                    y=sqrt(earth.a**2-(earth.a*earth.e)**2)*sin(t),
                    color=color.white)
    mercuryEllipse = curve(x=mercury.a*cos(t)-mercury.a*mercury.e,
                    y=sqrt(mercury.a**2-(mercury.a*mercury.e)**2)*sin(t),
                    color=color.white)
    venusEllipse = curve(x=venus.a*cos(t)-venus.a*venus.e,
                    y=sqrt(venus.a**2-(venus.a*venus.e)**2)*sin(t),
                    color=color.white)
    marsEllipse = curve(x=mars.a*cos(t)-mars.a*mars.e,
                    y=sqrt(mars.a**2-(mars.a*mars.e)**2)*sin(t),
                    color=color.white)
    jupiterEllipse = curve(x=jupiter.a*cos(t)-jupiter.a*jupiter.e,
                    y=sqrt(jupiter.a**2-(jupiter.a*jupiter.e)**2)*sin(t),
                    color=color.white)

#makes the celestial bodies move in orbit
    t1=0
    t2=0
    t3=0
    t4=0
    t5=0
    dt=0
    yearCount=0
    while 1:
        rate(1000)

        
        earth.accel = vector((sun.mass/(earth.a**2))*cos(radians(dt)),
                             (sun.mass/(earth.a**2))*sin(radians(dt)),0)
        earth.veloc += vector((sun.mass/(earth.a**2))*cos(radians(dt))*t1,
                             (sun.mass/(earth.a**2))*sin(radians(dt))*t1,0)
        earth.pos += (earth.veloc.x*radians(t1)*t1,
                      earth.veloc.y*radians(t1)*t1,0)
        
        mercury.pos = (mercury.a*cos(t2)-mercury.a*mercury.e,
                     sqrt(mercury.a**2-(mercury.a*mercury.e)**2)*sin(t2))
        venus.pos = (venus.a*cos(t3)-venus.a*venus.e,
                     sqrt(venus.a**2-(venus.a*venus.e)**2)*sin(t3))
        mars.pos = (mars.a*cos(t4)-mars.a*mars.e,
                     sqrt(mars.a**2-(mars.a*mars.e)**2)*sin(t4))
        jupiter.pos = (jupiter.a*cos(t5)-jupiter.a*jupiter.e,
                     sqrt(jupiter.a**2-(jupiter.a*jupiter.e)**2)*sin(t5))
        t1+= .1*radians(360)/365
        t2+= .1*radians(360)/88
        t3+= .1*radians(360)/225
        t4+= .1*radians(360)/687
        t5+= .1*radians(360)/4333
        dt+= .1*radians(360)/365.001
        if radians(dt) > 2*pi:
            dt=0
        yearCount+=1
        if yearCount == 100:
            print str(t1/radians(360)) + " Earth years"
            yearCount = 0

        
    
