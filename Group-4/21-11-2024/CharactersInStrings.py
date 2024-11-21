#Write a program to count the number of times a character occurs in a given string
string=input("Enter a string")
char=input("Enter a character")
count=0
for i in range(len(string)):
	if(string[i]==char):
		count=count+1
print("The total number of times",char,"has occured=",count)
