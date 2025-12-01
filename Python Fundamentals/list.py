# list1 = [1, 2, 7]
# list2 = [2, 4, 5]

# combined = list1 + list2
# avg = sum(combined) / len(combined)

# print(avg)


# Input two lists from the user
list1 = list(map(int, input("Enter elements of list 1 separated by space: ").split()))
list2 = list(map(int, input("Enter elements of list 2 separated by space: ").split()))

# Merge the lists
merged_list = list1 + list2

# Sort the result
merged_list.sort()

# Print result
print("Merged and Sorted List:", merged_list)

