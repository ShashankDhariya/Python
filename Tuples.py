# Tuples are immutable and are resided inside (). Also ' () ' are optional
marks = (80,84,93,94,94,95)
mark = 80,84,93,94,94,95        # Braces () are optional 

# marks[0] = 90       # Compiler will throw an error because tuples are immutable

print(marks)
print(mark)           # Printing tuple which is declared and initialised without ()


# Printing count and index of element in tuple
print(marks.count(95))      # O/p - 1 (It'll print the count of 95 in the tuple)
print(marks.index(95))      # O/p - 5 (It'll print the index of 95 in the tuple)