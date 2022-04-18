# Printing Hello Buddy
# Also semicoclon " ; " is optional in python 
print("Hello Buddy")



# Taking Input from the user 
# We Don't need to mention datatype while declaring variables in python
name = input("Enter your name : ")

# Concatenation of STRING with " + " sign   
print("Enered name is "+name)



# By default, In python every VARIABLE is inputed as String 
old_age = input("Enter your age : ")

# new_age = old_age + 2           # Here old_age variable is treated as string so will throw an error 

# But this problem can be resolved by explicit type conversion of old_age variable 
new_age = int(old_age) + 2        # Here error is resolved (by explicit type conversion of old_age variable)
print(new_age)

# Comments in Python 
#  " # " is used for single line comment whereas   '''   ''' is used for multiline comment

# This is single line comment
'''
This is multi line comment
'''

