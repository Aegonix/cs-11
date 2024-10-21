
#? WAP to take n employees names, designation, and salary.
#? Print the employee with highest salary and employee with lowest salary.

n = int(input("How many employees? "))

max = 0
min = max
max_name = ""
min_name = max_name

for i in range(n):
    salary = float(input("Enter salary of employee " + str(i + 1) + ": "))
    designation = input("Enter designation of employee " + str(i + 1) + ": ")
    name = input("Enter name of employee " + str(i + 1) + ": ")

    if not i:
        max = salary
        min = salary
        max_name = name
        min_name = name

    else:
        if salary > max:
            max = salary
            max_name = name

        if salary < min:
            min = salary
            min_name = name

print("Employee with highest salary is", max_name, "with salary of:", max)
print("Employee with lowest salary is", min_name, "with salary of:", min)
