str = "Tony Stark"



# Conversion of String to other forms 
# Converting to uperrcase 
print(str.upper())    # O/P - TONY STARK

# Converting to lowercase  
print(str.lower())    # O/P - tony stark

# Our original String is unaffected we changing the at some other memory location
print(str)

print(str.find("T"))    # It'll return index at which the char is in the String(if found) 
# otherewise it'll return -1
print(str.find("Stark"))



# Replacing string(or char) 
print(str.replace("Tony","Michael"))
print(str)


# Finding String pr character 
print("S" in str)       # It'll return true(in case found) or false(in case not found)
print("Stark" in str)   # True 
print("Michael" in str) # True 
print("Sk" in str)      # False 

