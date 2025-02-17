"""Arithemetic Operators"""

# Addition:  +
# Subtraction:  -
# Multiplication: *
# Exponent: **
# Division: /
# Floor Division: //
# Remainder: %


# Addition -->> +
X = 5
result = X + 8
print(result)
print(X + 88)


# Subtraction --->>> -
X = 9
result = X -99
print(result)


#Multiplication -->> *
Y = 55
result = Y *2
print(result)

# Exponent -->> **
A = 12
Exponent = A ** 2
print(f"Exponent-->> ** of 12 is : {Exponent}")

# Division -->> /
H = 44
Division = H / 22
print(f"Division of 44 is:{int(Division)}")

# Floor Division -->> //  -->> it round off the value to the nearest integers
S = 17 
FloorDiv = S // 2
print(f"Floor Division is {FloorDiv}")

#Concatination 
str1 = "Hey!"
str2 = " Shreenjal."
print(str1 + str2)


X = 5 
X += 10 # --> X = X + 10 
X -=  10 # --> X = X - 10 


'''Suppose you are a university student, and you need to pay $4535 tution fee for the next semester. The college is giving you a discout of 10% on the early payment of your tution fee. Since it's a good offer, you decided to make an early payment. Can you find out how much money you have to pay ?'''

fee = 4535
discount_percent = 10 
discount_amount = (discount_percent / 100) * fee 
discounted_fee = fee - discount_amount
print(discounted_fee)


'''Can you create a program to convert distance in kilometers to miles ?''' # Formula 1 km = 0.621371 miles1

distance_km = int(input("Enter distance in KM:"))
distance_miles = distance_km / 1.609
print(f" Distance in Miles is : {distance_miles}")


distances_km = int(input("Enter distance in KM:"))
conversion_ratio = 0.621371
distances_miles = distance_km * conversion_ratio
print(f" Distance in Miles is : {distances_miles}")



''' What we learned ?'''
# Equals operator (=) assigns the value in the right to the variable in left.
# Arithmetic operators peform basic arithmetic operations such as addition, subtraction, multiplication, etc.
# If we use the + operator with strings, it concatenates two strings.
# To make our code more readable, we can use the parentheses. For example, 34 * (88 - 9)