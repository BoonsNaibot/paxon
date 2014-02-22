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
        x, y = item
        
    A *= 0.5
    C_x *= 1.0/(6*A)
    C_y *= 1.0/(6*A)
    return (C_x, C_y)

A = [(3,0), (3,3), (5,3), (5,9)]
B = [(0,0), (0,9), (9,0), (9,9)]

a = to_polar(transform(A, 90, A[0]))
b = to_polar(transform(B, 90, A[0]))
b = to_polar(transform(B, 90, A[-1]))

"""
[(0.0,                 0.0), 
 (3.0,                 0.0), 
 (3.6055512754639891, -0.5880026035475675), 
 (9.2195444572928871, -0.21866894587394195)]
 
[(3.0,                 1.5707963267948966), 
 (9.486832980505138,   0.3217505543966422), 
 (6.0,                -1.5707963267948966), 
 (10.816653826391969, -0.5880026035475675)]
  
[(10.295630140987001,  2.6344941491974563), 
 (5.0,                 1.5707963267948966), 
 (9.8488578017961039, -2.7233683240105639), 
 (4.0,                -1.5707963267948966)]
"""
