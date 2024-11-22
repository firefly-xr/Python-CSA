# Calculates BMI and provides a category
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    return bmi, category

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi, category = calculate_bmi(weight, height)
print(f"Your BMI is {bmi:.2f} ({category}).")
