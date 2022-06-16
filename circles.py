# calcuate area and circumference of a circle based on user input

# Set base variables
welcome = "Welcome to circles.py!\nThis program will calculate the area and circumference of a circle."

radPrompt = "\n\nPlease enter the radius of the circle (in cm):  "

pi = 3.141529

# print welcome message
print(welcome)

# user input prompt
response = input(radPrompt)

# convert str to float
radius = float(response)

#Calculate circumference and area based on input
circumference = 2 * pi * radius
area = pi * (radius ** 2)

print(f"\nCircumference: {circumference}")
print(f"Area: {area}")


