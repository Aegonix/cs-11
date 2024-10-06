
#? 21.
#? Presume that a ladder is put upright against 
#? a wall. Let variables length and angle store   
#? the length of the ladder and the angle that 
#? it forms with the ground as it leans against  
#? the wall. Write a Python program to compute
#? the height reached by the ladder on the   
#? wall for the following values of length and angle:
#? a) 16 feet and 75 degrees 
#? b) 20 feet and 0 degrees 
#? c) 24 feet and 45 degrees
#? d) 24 feet and 80 degrees

from math import sin, pi

a = 75, 16
b = 0, 20
c = 45, 24
d = 80, 24

print(sin(a[0] * (pi / 180)) * a[1])
print(sin(b[0] * (pi / 180)) * b[1])
print(sin(c[0] * (pi / 180)) * c[1])
print(sin(d[0] * (pi / 180)) * d[1])
