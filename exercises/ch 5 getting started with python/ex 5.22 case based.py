
#? Case-based questions
#? Identify the personal details of students from your 
#? school identity card and write a program to accept these 
#? details for all students of your school and display them 
#? in the following format.

#

school_name = input("Enter school name: ")
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
class_ = input("Enter class: ")
section = input("Enter section: ")
address_1 = input("Enter address line 1: ")
address_2 = input("Enter address line 2: ")
city = input("Enter city: ")
pin = int(input ("Enter pin code: "))
phone = int (input("Enter the parent's phone number: "))

print(f"""
\t\t{school_name}
      
Student Name: {name}\t\tRollno: {roll}
Class: {class_}\t\t\tSection: {section}
Address: {address_1}
         {address_2}

City: {city}\t\tPin code: {pin}
Parent's/Guardian's contact no: {phone}""")
