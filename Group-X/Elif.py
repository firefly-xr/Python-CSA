# Example of elif to handle multiple conditions
choice = input("Enter a command (start, stop, exit): ")

if choice == "start":
    print("The program is starting.")
elif choice == "stop":
    print("The program is stopping.")
elif choice == "exit":
    print("Exiting the program.")
else:
    print("Invalid command.")
