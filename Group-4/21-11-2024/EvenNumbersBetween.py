# Program to display even numbers between two numbers given by the user
a=int(input("Enter a number"))
b=int(input("Enter a number"))
for number in range(a,b):
    if number%2==0:
      print(number)
