#Write a program to accept a number from the user and print the multiplication table of that number using while loop
number=int(input("Enter the number for its multiplication table: "))

print(f"Multiplication table of {number} up to 10th term:")

for i in range(1, 11):
      print(f"{number} x {i} ={number * i}")

#Write your code here
