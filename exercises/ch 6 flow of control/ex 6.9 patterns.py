
#? 9.
#? Write a program to print the following patterns:
#? i)
#*        *
#*      * * * 
#*    * * * * *
#*      * * * 
#*        * 
#? ii) 
#*            1
#*          2 1 2
#*        3 2 1 2 3 
#*      4 3 2 1 2 3 4 
#*    5 4 3 2 1 2 3 4 5 
#? iii)
#*    1 2 3 4 5
#*          1 2 3 4 
#*         1 2 3 
#*            1 2
#*                1
#? iv)
#*        *
#*      *   *
#*    *       * 
#*      *   *
#*        * 

#! i)

n = int(input())

for i in range(1, n + 1, 2):
    print(" " * (n - i) + "* " * i)

for i in range(n + 1, -1, -2):
    print(" " * (n - i) + "* " * i)
