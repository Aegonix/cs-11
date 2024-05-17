
#? 11.
#? Write a Python program to calculate the amount 
#? payable if money has been lent on simple interest. 
#? Principal or money lent = P, Rate of interest = R% 
#? per annum and Time = T years.
#? Then Simple Interest (SI) = (P x R x T)/ 100. 
#? Amount payable = Principal + SI.
#? P, R and T are given as input to the program.

P = float(input("Principal amount: "))
R = float(input("Interest rate (%): "))
T = float(input("Time (years): "))

print("Amount payable:", P + ((P * R * T) / 100))
