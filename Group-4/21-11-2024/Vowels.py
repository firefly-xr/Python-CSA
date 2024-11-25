#Write a program to count the number of vowels in a word
     #Example: enter a vowel: apple
     #                Count:2

#Write your code here

s=input("enter your string:") 
c=0
for i in s:
     if i in 'AEIOUaeiou' :
          c=c+1
print("count", c) 

