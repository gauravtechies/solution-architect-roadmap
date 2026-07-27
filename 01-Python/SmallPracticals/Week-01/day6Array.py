# Try these yourself:

# Create a list of 5 numbers.
# Print the first and last element.
# Find the length of the list.
# Add a new element using append().
# Insert an element at index 2.
# Remove an element using remove().
# Remove the last element using pop().
# Find the largest, smallest, and sum of elements.
# Print only even numbers from a list.
# Count how many even and odd numbers are in a list.
# Reverse a list.
# Sort a list in ascending order.


#  Create a list of 5 numbers.
numbers=[1,2,3,4,5]
numberss=[2,3,5,8,10,23,12,435,63,65347,765]

# Print the first and last element.
print("this is first number", numbers[0])
print("this is second number", numbers[-1])
print("this is length of list", len(numbers))
numbers.append("Gaurav")


# Insert an element at index 2.
numbers.insert(2,"Gaurav")
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers,"pop")

max_number=max(numberss)
min_number=min(numberss)
print(min_number)
print(max_number)

added_elements=sum(numberss)
print(added_elements)

# Print only even numbers from a list.
for d in numberss:
    if d%2==0:
       print("Even number")
       
       
# Count how many even and odd numbers are in a list.
count=0
for d in numberss:
    if d%2==0:
       count+=1
       print("Even number")
print(count," are even numbers")
print(len(numberss)-count, "are odd numbers")

#  Reverse a list.
numberss.reverse()
print(numberss)
       
numberss.sort()
print(numberss)
