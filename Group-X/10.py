# Function to check if a number is an Armstrong number
def is_armstrong(number):
    # Convert the number to a string to calculate the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    # Calculate the sum of the digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number

# Input from the user
num = int(input("Enter a number: "))

# Check and display result
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
