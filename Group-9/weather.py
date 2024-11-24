#program to print the precautions to take during different weathers
#First letter of weather should be written in capital letter
weather=input("Enter a weather: ")
match weather: 
    case 'Sunny':
      print("Wear Sunglasses")
    case 'Rainy':
      print("Wear a raincoat")
    case 'Snowy':
      print("Wear a sweatshirt")
    case 'Windy':
      print("Wear a coat")
    case _:
      print("Wear a T-Shirt")
