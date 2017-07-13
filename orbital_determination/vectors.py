#calculates the magnitude of an n-dimensional vector
def mag(v):
    sum = 0
    for n in v:
        sum += n**2
    return sum**0.5

#calculates the dot product of v and u
def dot(v,u):
    sum = 0
    count = 0
    for n in v:
        sum += n*u[count]
        count += 1
    return sum

#computes the cross product of V x U
def cross(v,u):
    x = v[1]*u[2] - v[2]*u[1]
    y = v[2]*u[0] - v[0]*u[2]
    z = v[0]*u[1] - v[1]*u[0]
    return [x,y,z]
