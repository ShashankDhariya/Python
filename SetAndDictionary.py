# Sets are resided inside {} 
'''
- Unordered Sequence 
- No duplicate elements are allowed 
- Index doesn't have any existance in sets 
'''

marks = {89,88, 89, 90, 87, 88}
print(marks)        # O/p - {88, 89, 90, 87} (as no duplicacy is allowed)

# print(marks[0])     # It'll throw an error as sets doesn't allow the use of index
# Index doesn't exist in set




# Dictionary 

marks1 = {"Physics" : 93, "Chemistry" : 84, "Maths" : 80}
print(marks1)

# Changing the data
marks1["Physics"] = 99
print(marks1)