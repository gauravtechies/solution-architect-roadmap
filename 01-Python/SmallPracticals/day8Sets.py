# Create a set of five numbers.
Students_interview_marks={23,45,12,45,66,32,43,12,43,65,11}
# Add one new number.
Students_interview_marks.add(44)
print(set(Students_interview_marks))
# Add multiple numbers using update().
Students_interview_marks.update([100,99,88])
print(Students_interview_marks)
# Remove a number using remove().
Students_interview_marks.remove(100)
print(Students_interview_marks) 
# Remove a number using discard().
Students_interview_marks.discard(100)
# Remove a random element using pop().
Students_interview_marks.pop()
# Find the length of a set.
print(len(Students_interview_marks))
# Find the largest, smallest, and sum of elements.
print(max(Students_interview_marks))
# Remove duplicates from a list using a set.
duplicatedSet=[12,12,43,12,45,54,65]
set_got_uniqued=set(duplicatedSet)
print(set_got_uniqued)
# Find the union of two sets.
union_of_Set=(set_got_uniqued | Students_interview_marks)
print(union_of_Set)
# Find the intersection of two sets.
intersection_of_Set=(set_got_uniqued & Students_interview_marks)
print(intersection_of_Set)
# Find the difference of two sets.
difference_of_Set=set_got_uniqued - Students_interview_marks
print(difference_of_Set)

# Find the symmetric difference.
symmetric_of_Set=set_got_uniqued ^ Students_interview_marks
print(symmetric_of_Set)
# Check whether one set is a subset of another.
print(set_got_uniqued.issubset(Students_interview_marks))
# Check whether one set is a superset of another.
print(Students_interview_marks.issuperset(set_got_uniqued))