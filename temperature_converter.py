# Temperature Converter

number = float(input("Please enter a temperature: "))
unit1 = int(input("Please enter the unit you are using (1-3):\n1. Celsius\n2. Fahrenheit\n3. Kelvin\n"))
unit2 = int(input("Please enter the unit you want to convert to (1-3):\n1. Celsius\n2. Fahrenheit\n3. Kelvin\n"))

def conversion(number, unit1, unit2):
    if unit1 == unit2:
        print(f"{number:.2f} in the same unit is still {number:.2f}")
        return

    result = None

    if unit1 == 1:  # Celsius
        if unit2 == 2:
            result = (number * 9/5) + 32
            print(f"{number:.2f} °C is equivalent to {result:.2f} °F")
        elif unit2 == 3:
            result = number + 273.15
            print(f"{number:.2f} °C is equivalent to {result:.2f} K")

    elif unit1 == 2:  # Fahrenheit
        if unit2 == 1:
            result = (number - 32) * 5/9
            print(f"{number:.2f} °F is equivalent to {result:.2f} °C")
        elif unit2 == 3:
            result = ((number - 32) * 5/9) + 273.15
            print(f"{number:.2f} °F is equivalent to {result:.2f} K")

    elif unit1 == 3:  # Kelvin
        if unit2 == 1:
            result = number - 273.15
            print(f"{number:.2f} K is equivalent to {result:.2f} °C")
        elif unit2 == 2:
            result = (number - 273.15) * 9/5 + 32
            print(f"{number:.2f} K is equivalent to {result:.2f} °F")
    
    else:
        print("Error: Please select units between 1 and 3.")

conversion(number, unit1, unit2)
