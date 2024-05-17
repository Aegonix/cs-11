
#? 9.
#? A dartboard of radius 10 units and the wall it is 
#? hanging on are represented using a two-dimensional 
#? coordinate system, with the board’s center at 
#? coordinate (0,0). Variables x and y store the 
#? x-coordinate and the y-coordinate of a dart that 
#? hits the dartboard. Write a Python expression using 
#? variables x and y that evaluates to True if the dart 
#? hits (is within) the dartboard, and then evaluate the 
#? expression for these dart coordinates:
#?  a) (0,0)
#?  b) (10,10)
#?  c) (6, 6) 
#?  d) (7,8)

x = int(input("X coordinate: "))
y = int(input("Y coordinate: "))

print(10 > ((x ** 2 + y ** 2) ** (1/2)))
