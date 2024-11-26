rows = int(input("Enter number of rows: "))

y = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while y!=(2*i-1):
        print("* ", end="")
        y += 1
    y=0
    print()
