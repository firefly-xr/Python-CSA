# Program to check if a number is an Armstrong number

# Input a number from the user
num = int(input("Enter a number: "))

# Convert the number to a string to find the number of digits
num_digits = len(str(num))

# Initialize a variable to store the sum of powers
sum_of_powers = 0

# Copy of the original number to work with
temp = num

# Loop to calculate the sum of each digit raised to the power of num_digits
while temp > 0:
    digit = temp % 10  # Get the last digit
    sum_of_powers += digit ** num_digits  # Add the digit raised to the power
    temp //= 10  # Remove the last digit

# Check if the sum of powers equals the original number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
