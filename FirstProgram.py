unsorted_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]  # define unsorted list
sorted_ascending_list = unsorted_list.copy()  # declaring list with first list's elements
sorted_ascending_list.sort()  # sorting list in ascending way
sorted_descending_list = unsorted_list.copy()  # declaring list with first list's elements
sorted_descending_list.sort(reverse=True)  # sorting list in descending way
print("Unsorted list is:", unsorted_list, "\nSorted ascending list is:", sorted_ascending_list, "\nSorted descending list is", sorted_descending_list)

print("Even numbers from list are:", sorted_ascending_list[1::2])
print("Odd numbers from list are:", sorted_ascending_list[0::2])
print("Multiples of 3 are:", [x for x in sorted_ascending_list if x % 3 == 0])
