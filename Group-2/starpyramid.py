rows = int(input("Enter number of rows: "))

x = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        x += 1
   
    x = 0
    print()
