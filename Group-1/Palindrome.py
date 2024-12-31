#To check whether a number is a palindrome or not

num=int(input("Enter a number: "))
temp=num
rev=0
while(temp>0):
  r=temp%10
  temp=temp//10
  rev=rev*10+r
print(f"Reverse of {num} is {rev}")
if rev==num:
   print(f"{num} is a palindrome")
else:
   print(f"{num} is not a palindrome")




