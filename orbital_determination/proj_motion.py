from visual import *
from math import *
from vectors import *

#simulates projectile motion in free fall
def projFF(spd,ang):
    ang = radians(ang)

    #define objects
    proj = sphere(pos=vector(0,0,0), radius=1, color=color.red)

    proj.velocity = vector(spd*cos(ang),spd*sin(ang),0)
    proj.trail = curve(color=color.white)
    vel = arrow(pos=proj.pos, axis=0.25*proj.velocity, color=color.white)

    d = 0
    t = 0
    dt = 0.001

    #adjust velocity and position
    while proj.pos.y >= 0:
        rate(2900)
        proj.pos += proj.velocity*dt
        proj.velocity += (0,-9.8*dt,0)
        proj.trail.append(pos=proj.pos)
        vel.pos = proj.pos
        vel.axis = proj.velocity*0.25
        t += dt

    print "Range: " + str(proj.pos.x) + " meters"
    print "Time of Flight: " + str(t) + " seconds"

#simulates projectile motion with air resistance
def proj(spd,ang,c):
    ang = radians(ang)

    #define objects
    proj = sphere(mass = 1.0, pos=vector(0,0,0), radius=0.1, color=color.red)

    proj.velocity = vector(spd*cos(ang),spd*sin(ang),0)
    proj.accel = vector(-c*spd*proj.velocity.x/proj.mass,-9.8 - c*spd*proj.velocity.y/proj.mass,0)
    proj.trail = curve(color=color.white)
    vel = arrow(pos=proj.pos, axis=0.5*proj.velocity, color=color.white)

    d = 0
    t = 0
    dt = 0.001

    #adjusts position, velocity, and acceleration
    while proj.pos.y >= 0:
        rate(2900)
        proj.pos += proj.velocity*dt
        proj.accel.x = -c*mag(proj.velocity)*proj.velocity.x/proj.mass
        proj.accel.y = -9.8 - c*mag(proj.velocity)*proj.velocity.y/proj.mass
        proj.velocity += (proj.accel.x*dt,proj.accel.y*dt,0)
        proj.trail.append(pos=proj.pos)
        vel.pos = proj.pos
        vel.axis = proj.velocity*0.5
        t += dt

    print "Range: " + str(proj.pos.x) + " meters"
    print "Time of Flight: " + str(t) + " seconds"
