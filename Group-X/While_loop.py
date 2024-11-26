# Example of a while loop to display a menu
while True:
    print("\n=== Menu ===")
    print("1. Option One")
    print("2. Exit")
    choice = input("Enter your choice (1-2): ")
    if choice == "1":
        print("You selected Option One.")
    elif choice == "2":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
