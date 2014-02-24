from math import cos, sin, sqrt, atan2

def transform(l, angle, first):
    #C = cos(angle)
    #S = sin(angle)
    C, S = angle
    
    return [((((first[0]-item[0])*C) - ((first[1]-item[1])*S)), (((first[0]-item[0])*S) + ((first[1]-item[1])*C))) for item in l]

def to_polar(l):
    return [(sqrt((item[0]**2)+(item[1]**2)), atan2(item[1], item[0])) for item in l]
    
def centroid(l):
    C_x = C_y = A = x = y = 0
    
    for item in l:
        A += ((x*item[1])-(item[0]*y))
        C_x += ((x+item[0])*A)
        C_y += ((y+item[1])*A)
        x, y = item
        
    A *= 0.5
    C_x *= 1.0/(6*A)
    C_y *= 1.0/(6*A)
    return (C_x, C_y)

A = [(3,0), (3,3), (5,3), (5,9)]
B = [(0,0), (0,9), (9,0), (9,9)]

a = to_polar(transform(A, (0, 1), A[0]))
b = to_polar(transform(B, (0, 1), A[0]))
c = to_polar(transform(A[::-1], (0,-1), A[-1]))
d = to_polar(transform(B, (0,-1), A[-1]))
print a
print b
print c
print d

"""
[(0.0,                 0.0), 
 (3.0,                 0.0), 
 (3.6055512754639891, -0.5880026035475675), 
 (9.2195444572928871, -0.21866894587394195)]
 
 [(3.0,                 1.5707963267948966), 
  (9.4868329805051381,  0.32175055439664219), 
  (6.0,                -1.5707963267948966), 
  (10.816653826391969, -0.5880026035475675)]
  
[(0.0,                 0.0), 
 (6.0,                 0.0), 
 (6.324555320336759,  -0.32175055439664219), 
 (9.2195444572928871, -0.21866894587394195)]

[(10.295630140987001, -0.50709850439233695), 
 (5.0,                -1.5707963267948966), 
 (9.8488578017961039,  0.41822432957922911), 
 (4.0,                 1.5707963267948966)]
"""
