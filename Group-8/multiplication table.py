multiplication_table(number):
    for i in range(1, 11): 
        print(f"{number} x {i} = {number * i}")
num = int(input("Enter a number to print its multiplication table: "))
