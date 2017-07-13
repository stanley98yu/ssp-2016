from visual import *
from vectors import *

#creates a 3-body orbit simulator that includes interactions between bodies
def threeBody():
    #constants
    G = .667408
    dt = 0.01
    n=0
    
    #initializes the orbital bodies and their trails
    body1 = sphere(pos=vector(0,0,0), radius= 10, m=100000, v=vector(0,0,0),
                   a=vector(0,0,0), color=color.yellow)
    body2 = sphere(pos=vector(40,0,0), radius=0.5, m=100, v=vector(0,30,0),
                   a=vector(0,0,0), color=color.red)
    body3 = sphere(pos=vector(41,0,0), radius=0.5, m=1, v=vector(0,35,0),
                   a=vector(0,0,0), color=color.green)
    body1.trail = curve(color=color.white)
    body2.trail = curve(color=color.white)
    body3.trail = curve(color=color.white)

    while 1:
        rate(100)
        #finds distances between bodies
        d12 = mag(body1.pos-body2.pos)
        d13 = mag(body1.pos-body3.pos)
        d23 = mag(body2.pos-body3.pos)
        u12 = norm(body1.pos-body2.pos)
        u21 = -u12
        u13 = norm(body1.pos-body3.pos)
        u31 = -u13
        u23 = norm(body2.pos-body3.pos)
        u32 = -u23

        #calculates the forces due to gravity between bodies
        f12 = (G*body2.m*body1.m)/(d12**2)
        f13 = (G*body3.m*body1.m)/(d13**2)
        f23 = (G*body2.m*body3.m)/(d23**2)

        #updates the positions of the bodies
        body1.pos += dt*body1.v+(.5*dt**2)*((f12/body1.m)*u21+(f13/body1.m)*u31)
        body2.pos += dt*body2.v+(.5*dt**2)*((f12/body2.m)*u12+(f23/body2.m)*u32)
        body3.pos += dt*body3.v+(.5*dt**2)*((f13/body3.m)*u13+(f23/body3.m)*u23)

        #updates the velocities of the bodies
        body1.v += .5*(f12/body1.m*u21)*dt
        body1.v += .5*(f13/body1.m*u31)*dt
        body2.v += .5*(f12/body2.m*u12)*dt
        body2.v += .5*(f23/body2.m*u32)*dt
        body3.v += .5*(f23/body3.m*u23)*dt
        body3.v += .5*(f13/body3.m*u13)*dt

        #updates the trails
        body1.trail.append(pos=body1.pos)
        body2.trail.append(pos=body2.pos)
        body3.trail.append(pos=body3.pos)

        n+=1
        if n%100 == 0:
            KE = 0
            KE += .5*body1.m*(mag(body1.v)**2)
            KE += .5*body2.m*(mag(body2.v)**2)
            KE += .5*body3.m*(mag(body3.v)**2)
            PE = 0
            PE -= G*body1.m*body2.m/d12
            PE -= G*body1.m*body3.m/d13
            PE -= G*body2.m*body3.m/d23
            print KE + PE

        

        
