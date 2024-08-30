
#? WAP to print the following pattern:
#* P
#* PY
#* PYT
#* PYTH
#* PYTHO
#* PYTHON

x = "PYTHON"

for i in range(1, len(x) + 1):
    for j in range(i):
        print(x[j], end="")
    
    print()
