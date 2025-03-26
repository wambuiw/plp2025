numbers = input("enter numbers separate by space: ")
num_list = list(map(int,numbers.split()))

total = sum(num_list)
print(f"total sum  is: {total}")