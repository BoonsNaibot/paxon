from math import cos, sin, sqrt, atan2

def transform(l, angle, first):
    #C = cos(angle)
    #S = sin(angle)
    C = 0
    S = 1
    
    return [((((first[0]-item[0])*C) - ((first[1]-item[1])*S)), (((first[0]-item[0])*S) + ((first[1]-item[1])*C))) for item in l]

def to_polar(l):
    return [(sqrt((item[0]**2)+(item[1]**2)), atan2(item[1], item[0])) for item in l]
    
def centroid(l):
    C_x = C_y = A = x = y = 0
    
    for item in l:
        A += ((x*item[1])-(item[0]*y))
        C_x += ((x+item[0])*A
        C_y += ((y+item[1])*A
        
    A *= 0.5
    C_x *= 1.0/(6*A)
    C_y *= 1.0/(6*A)
    return (C_x, C_y)

A = [(3,0), (3,3), (5,3), (5,9)]
B = [(0,0), (0,9), (9,0), (9,9)]

a = to_polar(transform(A, 90, A[0]))
b = to_polar(transform(B, 90, B[0]))
