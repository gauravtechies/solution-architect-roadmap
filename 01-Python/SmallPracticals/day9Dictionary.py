# Try these yourself:

# Create a dictionary for a student (name, age, marks).
students={
    "student1":{
        "name":"Gaurav",
        "age":33,
        "marks":83
    },
    "student2":{
         "name":"Gudden",
          "age":33,
          "marks":88
    }
}
# Print the student's name.
for key,value in students.items():
    print(value["name"],"->",value["age"])

# Print the student's age using get().
for key,value in students.items():
    print(value.get("name"))
# Add a new key "city".
students["student1"].update({"city":"Ludhiana"})
print(students["student1"])
# Update the marks.
students["student1"]["marks"]=93
print(students)
# Remove "city" using pop().
students["student1"].pop("city")
print(students)
# Print all keys.
for key,values in students.items():
    print(key)
    for childkeys in values:
        print(childkeys)
  
    #  Alternate way to print keys and good way
for student in students.values():
    print(student.keys(),"Greate approach by gpt")
# Print all values.
for key,values in students.items():
    print(values["name"])
    print(values["age"])
    print(values["marks"])
# Print all key-value pairs using items().
for key,values in students.items():
    print(key,values)
    for key,value in values.items():
        print(key,value)
# Check if "name" exists.
for key,values in students.items():
    if "name" in values:
        print(values["name"])
    else:
        print("no name exist")
    
    
# Find the length of the dictionary.
print(len(students))
# Copy the dictionary.
copiedStudents=students.copy()
print(copiedStudents)
# Clear the copied dictionary.
copiedStudents.clear()
print(copiedStudents)
# Create a nested dictionary for two students.
students={
    "student1":{
        "name":"Gaurav",
        "age":33,
        "marks":83
    },
    "student2":{
         "name":"Gudden",
          "age":33,
          "marks":88
    }
}
# Print the marks of the second student.
print(students["student2"].get("marks"))