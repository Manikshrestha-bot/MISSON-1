'''While Loop'''
count = 0
'''Infinite loop'''
while count < 5:                        
    print("I am inside a loop.")
    print('Looping is interesting.')



count = 5

while count <= 10:
    # print(" I am while loop")
    count = count + 1

number = int(input("Enter a number:"))

count = 1

while count <=10:
    product = number * count
    print(product)
    count = count + 1

num = int(input("Enter a number : "))

value = -1
while value >= -10:
    product = num * value 
    print( num, "X" ,value,"=", product)
    value = value - 1

''' Can you modify the multiplication table program so that we get a multiplication table from 10 to 1 instead of 1 to 10 ?'''
num = int(6)

count = 10 
while count >= 1:
    product = num * count
    print( num, "*", count, "=", product)
    count = count - 1


''' What we learned?'''
# Loops are used in programming to repeat a block of code.
# The while loop runs continuoulsy unti the test condition evalutes to false.
# If the test condition of the loop is never false, the loop runs infinitely until the memory runs out. This is known as the infinite loop.