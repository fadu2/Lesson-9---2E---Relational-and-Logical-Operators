# Boolean: Relational and Logical Operators
# Relational operators 

# > greater than
# < less than
# >= greater or equal to 
# <= less or equal to 
# == equal to 
# != not equal to 

a = 4
b = 3

print(a > b)  # True 
print(a < b)  # False 
print(a >= b) # True 
print(a <= b)  # False 
print(a == b)  # False 
print(a != b)  # True 

# boolean expression 
c = 4 > 2
print(c) # True 

# Logical operators - used to combine 2 or more boolean expressions 
# and 
# or 
# not 

d = 4 > 2 and 3 < 1 # True and False = False 
print(d)  # False 

# Truth Table 
# T and T = T 
# T and F = F 
# F and T = F 
# F and F = F 

# T or T = T 
# T or F = T 
# F or T = T 
# F or F = F 

# not True is False 
# not False is True 
print(not(4 > 2))  # False 
print(not(3 < 1))  # True 

print(not(3<=3) and (4>2)) # False 
print(not(78>32) or (45<34))  # F or F = F 

print(not(2 >= 5) or not(5 > 3))  # T or F = T 

age = int(input("Enter your age: "))
drivingAge = 16 
canDrive = age >= drivingAge 
print("Can the person drive?", canDrive)










