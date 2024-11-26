num = int(input("Enter the number: "))

if num <= 1:
    print('Number is not a prime number.')
else:
    prime_value = True 
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime_value = False 
            break 
    
    if prime_value:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


