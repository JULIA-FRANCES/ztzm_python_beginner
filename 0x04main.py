#Milestone Project 1: Simple Unit Converter

print("Welcome to the Simple Unit Converter!")
print("Choose a conversion type:")
print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")
print("3. Grams to Pounds")

# Get the user's choice
choice = input("Enter your choice (1/2/3): ")

# Choice 1: Kilometers to Miles 
if choice == "1":
    kilometers = float(input("Enter distance in kilometers: "))
    # Conversion factor: 1 kilometer = 0.621371 miles
    miles = kilometers * 0.621371
    print(f"{kilometers:.1f} km is equal to {miles:.2f} miles.")

# Choice 2: Celsius to Fahrenheit
elif choice == "2":
    celsius = float(input("Enter temperature in Celsius: "))
    # Formula: (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.1f}°C is equal to {fahrenheit:.1f}°F")

#  Choice 3: Grams to Pounds 
elif choice == "3":
    grams = float(input("Enter weight in grams: "))
    # Conversion factor: 1 gram = 0.00220462 pounds
    pounds = grams * 0.00220462
    print(f"{grams:.1f} g is equal to {pounds:.2f} lbs.")

#  Handle Invalid Input 
else:
    print("Invalid choice! Please restart the program and enter 1, 2, or 3.")