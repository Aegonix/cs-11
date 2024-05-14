
#? 12.
#? work will be completed by three persons A, B and 
#? Write a program to calculate in how many days a 
#? C together. A, B, C take x days, y days and z days 
#? respectively to do the job alone. The formula to 
#? calculate the number of days if they work together 
#? is xyz/(xy + yz + xz) days where x, y, and z are given 
#? as input to the program.

x = int(input("Days for person A: "))
y = int(input("Days for person B: "))
z = int(input("Days for person C: "))

print("Total days:", (x * y * z) / ((x * y) + (y * z) + (x * z)))
