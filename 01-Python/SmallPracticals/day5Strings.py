# https://docs.google.com/document/d/1oeeQf_OkqgxglbDB5BxAp1POCwjxTRgMUObAsZACk1Y/edit?tab=t.x1amo12qofe2
# #Reverse a string using a for loop
# def reverse_string(text):
#     reversed_text = ""
#     for char in text:
       
#         reversed_text = char + reversed_text  # Prepend character
#         print(f"Current character: {char}, Reversed text so far: {reversed_text}")
#     return reversed_text,get_rever


# print(reverse_string("Python"))  # Output: nohtyP


# Print the first and last character of a string.
print_any_number=str(input("Enter some string: "))
first_element=print_any_number[0]
second_element=print_any_number[-1]
print("First Element of the String is:",first_element)
print("Last Element of the String is:",second_element)


# Print the length of a string.
length_of_string=len(print_any_number)
print(length_of_string)

# Convert a string to uppercase and lowercase.
get_uppercase=print_any_number.upper()
print(get_uppercase)

# Count vowels in a string.
vowel_count=0
for d in str(print_any_number):
    
    if d in "aeiou":
        vowel_count+=1
        print("Vowel")
    else:
        print("Not a vowel")

print(f"Total vowels in the string: {vowel_count}")

# Reverse a string.
print(f"Reversed string: {print_any_number[::-1]}")

reversed_string=""
for d in str(print_any_number):
    reversed_string=d+reversed_string
    
print(reversed_string)

# Check if a string is a palindrome.
if print_any_number==print_any_number[::-1]:
   print("Its palindrome")
else:
   print("Its not palindrome")

# Count how many times a character appears.
print(print_any_number.count("a"))

# Replace one word with another.
print(print_any_number.replace("a","u"))

# Split a sentence into words.
print(print_any_number.split())

# Print each character of a string using a for loop.
for d in str(print_any_number):
    print(d)
