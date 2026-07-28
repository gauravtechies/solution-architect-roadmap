# Create a tuple of five numbers.
created_tupple=(2,1,3,4,4)
List=[1,3,13,4,2,4]

# Print the first and last element.
print(created_tupple[0])
print(created_tupple[-1])
# Find the length of a tuple.
print(len(created_tupple))
# Count how many times a value appears.
print(created_tupple.count(4))
# Find the index of a value.
print(created_tupple.index(4),"Index")
# Find the largest and smallest number.
print(max(created_tupple))
# Find the sum of all elements.
print(sum(created_tupple))
# Loop through a tuple.
for tupple in created_tupple:
    print(tupple,"Travrsed")
# Convert a list into a tuple.
t=tuple(List)
print(type(t))
# Convert a tuple into a list.
L=list(created_tupple)
print(type(L))
# Swap two variables using tuple unpacking.
a=12
b=13
a,b=b,a
print(a)
print(b)
# Create a single-element tuple.
singlt_element_tupple=(13,)
print(type(singlt_element_tupple))
