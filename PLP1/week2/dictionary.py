#empty dictionary
person_info = {}

#input
person_info["name"] = input("Enter your name: ")
person_info["age"] = int(input("Enter your age: "))  # Convert to an integer
person_info["favorite_color"] = input("Enter your favorite color: ")


print("\nHere is your stored information:")
print(person_info)
