def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Number is divisible by a number other than 1 and itself
    return True

# Input from the user
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
