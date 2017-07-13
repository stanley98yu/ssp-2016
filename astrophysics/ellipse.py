from visual import *
from visual.graph import *

#creates an ellipse centered at the origin
def ellipse1():
    a = input("Enter the semi-major axis: ")
    b = input("Enter the semi-minor axis: ")

    gd = gdisplay(width=600,height=600,xmax=1.25*a,xmin=-1.25*a,
                  ymax=1.25*a,ymin=-1.25*a)

    e = gcurve(color=color.white)
    for x in arange(-a,a,0.01):
        e.plot(pos=(x,sqrt(b**2*(1-(x/a)**2))))
    for x in arange(a,-a,-0.01):
        e.plot(pos=(x,-sqrt(b**2*(1-(x/a)**2))))

#craetes plots of different ellipses with varying eccentricities and a's
def ellipse2():
    n = input("Enter the number of ellipses: ")
    i=0
    e = []
    a = []
    while i < n:
        e += [input("Enter eccentricity: ")]
        a += [input("Enter semi-major axis: ")]
        i+=1

    gd1 = gdisplay(width=600,height=600,xmax=2*a[0],xmin=-2*a[0],
                  ymax=2*a[0],ymin=-2*a[0])

    for j in e:
        graph = gcurve(color=color.white)
        b2 = a[0]**2 - (a[0]*j)**2
        for x in arange(-a[0],a[0],0.001):
            graph.plot(pos=(x+a[0]*j,sqrt(b2*(1-(x/a[0])**2))))
        for x in arange(a[0],-a[0],-0.001):
            graph.plot(pos=(x+a[0]*j,-sqrt(b2*(1-(x/a[0])**2))))
    
    gd2 = gdisplay(width=600,height=600,xmax=2*max(a),xmin=-2*max(a),
                  ymax=2*max(a),ymin=-2*max(a))
    for k in a:
        graph = gcurve(color=color.white)
        b2 = k**2 - (k*e[0])**2
        for x in arange(-k,k,0.001):
            graph.plot(pos=(x+k*e[0],sqrt(b2*(1-(x/k)**2))))
        for x in arange(k,-k,-0.001):
            graph.plot(pos=(x+k*e[0],-sqrt(b2*(1-(x/k)**2))))
