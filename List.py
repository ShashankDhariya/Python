# Lists resides inside square brackets-[]
 
marks = [99,55,67,97]
print(marks)

# Indexing in list
print(marks[0])     # O/p - 99 (Indexing starts from 0)

# Index can also be negative value

print(marks[-1])    # O/p - 97 (Last index can be pointed by index value -1)
print(marks[-2])    # O/p - 67
print(marks[-3])    # O/p - 55
print(marks[-4])    # O/p - 99

'''
  0      1     2     3    Positive index
[99     55    67    99]
 -4     -3    -2    -1    Negative index
'''

# Printing in range
print(marks[1:3])       # It excludes 3(index)

# Appending new data to list 
marks.append(90)      # This function will append data to the last of the list at last index
# O/p - [99, 55, 67, 99, 90]
print(marks)

# Searching data in the List
print(99 in marks)      # O/p - True
print(89 in marks)      # O/p - False

# Getting length of the list 
print(len(marks))       # O/p - 5

i = 0 
while(i<len(marks)) : 
    print(marks[i])
    i += 1

# Clearing the list to no elements in the list
marks.clear()
print(marks)        # [] - Empty list

# Quick Exercise 
# 1) Print name if found and 2) Print every name other than searched name
student = ["Shashank", "Mayank", "Ajay", "Mack"]
print(student)

for name in student :
    if(name == "Shashank"):
        print(name+" found")

for name in student : 
    if(name == "Shashank"):
        continue;
    else:
        print(name)