if __name__ == "__main__":
  # Get user's name
  name = input("Enter your name: ")

  # Get user's age and convert it to an integer (as input returns a string)
  age = int(input("Enter your age: "))

  # Get user's location
  location = input("Enter your location: ")

  # Print personalized message using f-strings for cleaner formatting
  print(f"Hello {name}, you are {age} years old and live in {location}.")