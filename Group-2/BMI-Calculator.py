# Get user input for weight and height
weight = float(input("Enter weight in kg: "))  # Convert input to float
height = float(input("Enter height in meters: "))  # Convert input to float

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI category
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obese")
	
