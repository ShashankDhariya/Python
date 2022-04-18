a = input("Enter first number : ")
b = input("Enter second number : ")
sum = a + b

print("String sum "+sum)
sum = int(a) + int(b)
# print("Sum is"+sum)       # This will throw error because Strings can't be concatenated with integer

print("Sum is "+str(sum))    # The problem can also be solved by making int(sum) to str(sum) so that concatenation can be occur



