# Pi defined as a float number
pi = 3.14159

# Convert user input from string to float
radius = float(input("Enter the radius of the circle: "))

# Calculate area using the formula: area = pi * radius^2
area = pi * (radius ** 2)

# Display the result rounded to 2 decimal places
print(f"The area of the circle is: {area:.2f}")