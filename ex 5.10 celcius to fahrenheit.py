
#? 10.
#? Write a Python program to convert temperature in 
#? degree Celsius to degree Fahrenheit. If water boils 
#? at 100 degree C and freezes as 0 degree C, use the 
#? program to find out what is the boiling point and 
#? freezing point of water on the Fahrenheit scale. 
#? (Hint: T(°F) = T(°C) × 9/5 + 32)

celcius = float(input("Enter celcius: "))
fahrenheit = (celcius * (9/5)) + 32

print("Fahrenheit =", fahrenheit)
