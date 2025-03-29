#fruits = ["apple","banana","cherry"]

#for fruit in fruits:                    #for loop 
 #   print(f"I Love {fruit}!")

#for loop using range
#for number in range(1,7):
 #   print(f"number:{number}")

#while loop
#count = 1

#while count<=5:
   # print(f"count: {count}")
    #count +=1

#loop control: break and continue
#if number == 5:
 #       print("breaking the loop at 5")
  #      break

   # elif number %2 == 0:
    #    print(f"skipping {number} because its even")
     #   continue
    #print(f"Processing number: {number}")

#nested loops
#for i in range(1, 4):  # Outer loop
 #   for j in range(1, 4):  # Inner loop
  #      print(f"Outer loop: {i}, Inner loop: {j}")


#list comprehension
# Traditional loop
squares = []
for x in range(5):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# List comprehension with a condition
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

 #Create a 3x3 matrix using nested list comprehensions
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

#transforming data
names = ["Alice", "Bob", "Charlie"]
uppercased_names = [name.upper() for name in names]
print(uppercased_names)  # Output: ['ALICE', 'BOB', 'CHARLIE']

#filtering data
numbers = [10, 15, 20, 25, 30]
divisible_by_5 = [num for num in numbers if num % 5 == 0]
print(divisible_by_5)  # Output: [10, 15, 20, 25, 30]

#flattening a list
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]