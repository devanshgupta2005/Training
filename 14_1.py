# ##
# numbers = [10, 20, 30, 40, 50]

# print("First element:", numbers[0])
# print("Last element:", numbers[-1])
# print("Length of list:", len(numbers))


# ## 
# numbers = [10, 20, 30, 40, 50]

# total = sum(numbers)
# average = total / len(numbers)

# print("Sum:", total)
# print("Average:", average)


# ##
# fruits = ["apple", "banana", "orange"]

# # Add a new fruit at the end
# fruits.append("mango")

# # Insert a fruit at position 2 (index 1)
# fruits.insert(1, "grapes")

# print(fruits)

# ##
# fruits = ["apple", "banana", "orange", "mango"]

# # Remove a specific element
# fruits.remove("banana")

# # Remove the last element
# fruits.pop()

# print(fruits)


# ##
# numbers = [1, 2, 3, 2, 4, 2, 5]

# count_2 = numbers.count(2)

# print("Number of times 2 appears:", count_2)

# ##
# numbers = [10, 20, 30, 40, 50]

# num = int(input("Enter a number: "))

# if num in numbers:
#     print("The number exists in the list.")
# else:
#     print("The number does not exist in the list.")


# ##
# numbers = [5, 10, 15, 20, 25]

# num = int(input("Enter a number to find its position: "))

# if num in numbers:
#     position = numbers.index(num)
#     print("The position of the number is:", position)
# else:
#     print("Number not found in the list.")


# ##
# numbers = [40, 10, 30, 20, 50]

# # Sort in ascending order
# numbers.sort()
# print("Ascending order:", numbers)

# # Sort in descending order
# numbers.sort(reverse=True)
# print("Descending order:", numbers)

# ##
# numbers = [1, 2, 3, 4, 5]

# numbers.reverse()

# print("Reversed list:", numbers)

# ##------------------------------------------------------------------------------------------------------
# numbers = (10, 20, 30, 40, 50)

# print("First element:", numbers[0])
# print("Last element:", numbers[-1])


# ##
# print("Length of tuple:", len(numbers))
# numbers = (10, 20, 30, 40, 50)

# ##
# fruits = ("apple", "banana", "cherry", "date", "elderberry")
# for fruit in fruits:
#     print(fruit)


# ##
# element = "banana"
# if element in fruits:
#     print(f"{element} exists in the tuple.")
# else:
#     print(f"{element} does not exist in the tuple.")

# ##
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# concatenated = tuple1 + tuple2
# print("Concatenated tuple:", concatenated)


# ##
# repeated_numbers = (1, 2, 2, 3, 4, 2, 5)
# count_2 = repeated_numbers.count(2)
# print("Number 2 appears", count_2, "times.")


# ##
# ten_integers = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
# pos = ten_integers.index(25)
# print("Position of 25 is:", pos)


# ##
# my_list = [100, 200, 300]
# converted_tuple = tuple(my_list)
# print("Converted tuple:", converted_tuple)


# ##
# original_tuple = (1, 2, 3)
# temp_list = list(original_tuple)
# temp_list.append(4)  # Modify list
# modified_tuple = tuple(temp_list)
# print("Modified tuple:", modified_tuple)


# ##
# nested_tuple = (1, 2, (3, 4, 5), 6)
# print("Nested tuple:", nested_tuple)

# # Print elements including nested ones:
# for element in nested_tuple:
#     if isinstance(element, tuple):
#         for sub_element in element:
#             print("Nested element:", sub_element)
#     else:
#         print("Element:", element)



