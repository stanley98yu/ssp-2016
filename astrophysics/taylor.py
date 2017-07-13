from visual import *
from visual.graph import *

#graphs the taylor series function for cos(x)
def taylor(N):
    #initializes a window for display
    gd = gdisplay(width=600,height=600,xmax=N,xmin=-N,
                  ymax=5,ymin=-5)

    series = ""
    s = 0
    #adds the number of terms to the equation
    for n in range(0,2*N,2):
        term = "(x**" +str(n)+ ")/factorial(" +str(n)+ ")"
        if s%2 == 0:
            series += term + " - "
            s += 1
        else:
            series += term + " + "
            s += 1
    series = series[:-3]
    print series

    #graphs the taylor series function
    g = gcurve(color=color.white)
    for x in arange(-N,N,.01):
        g.plot(pos=(x,eval(series)))
        
