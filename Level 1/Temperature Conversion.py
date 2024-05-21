# Task: Temperature Conversion
# Create a Python program that converts temperatures
# between Celsius and Fahrenheit.
# Prompt the user to enter a temperature value and the unit of measurement,
# and then display the converted temperature.
temp = float(input("Enter a temperature value: "))
while True:
    unit = input("Enter the unit of measurement (c/f): ")
    if unit.lower() == "c" or unit.lower() == "f":
        break
    else:
        print("Wrong Input")
print(f"Temperature is: {temp}°{unit.upper()}")

# Logic: C/5=(F-32)/9, so, C = (F - 32) * 5 / 9 and F = (9 * C / 5) + 32
if unit.lower() == "c":
    print("Converting the Temperature from Celsius to Fahrenheit :")
    temp = (9 * temp / 5) + 32
    unit = "F"
    print(f"Equivalent Fahrenheit Temperature is : {temp}°{unit}")
else:
    print("Converting the Temperature from Fahrenheit to Celsius :")
    temp = (temp - 32) * 5 / 9
    unit = "C"
    print(f"Equivalent Celsius Temperature is : {temp}°{unit}")

