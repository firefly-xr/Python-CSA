#Write a program to display the sum of even numbers and odd number s up to n entered by the user
 
#Write your code here

n=int(input("Enter a number:"))
o=0
e=0
for i in range (n):
        if i%2==0:
                e=e+i
        else:
                o=o+i
print("even=",e)
print("odd=",o)


