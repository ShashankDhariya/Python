age = int(input("Enter your age : "))

# if-else Statements
# While using Conditional statements there should be proper indentation for block of statements in the program
if(age >= 18) :
    print("You are adult now")
    print("So go for vote")
else :
    print("You're still a kid.")
    print("So don't indulge in political activities.")



# Range in python 
number = range(5)    # It excludes 5
print(number)

# Looping Statements - 1) for loop, 2)while loop

# 1) For Loop
for i in range(5) :     #if i is in the given range then goto block 
    print(i)

i = 0 
# 2) While Loop 
while(i<5):
    print(i)
    i += 1