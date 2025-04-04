#set 1 input
set1 = set(map(int, input("Enter numbers for the first set (separated by spaces): ").split()))

#set2 input
set2 = set(map(int, input("Enter numbers for the second set (separated by spaces): ").split()))

#intersection
common_numbers = set1 & set2  # This finds numbers in both sets


print("\nCommon numbers in both sets:", common_numbers)
