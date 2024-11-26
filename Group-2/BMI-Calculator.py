bmi = weight / (height ** 2)
if bmi < 18.5:
	print("Underweight")
elif 18.5 <= bmi < 24.9:
	print("Normal weight")
elif 25 <= bmi < 29.9:
	print("Overweight")
else:
	print("Enter Currect Digit")


weight = input("Enter weight in kg: ")
height = input("Enter height in meters: ")
