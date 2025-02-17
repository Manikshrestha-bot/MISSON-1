'''SEQUECES'''
'''  SEQUENCE IN PYTHON IS COLLECTION OF ITEMS IN AN ORDER'''
""" FOR LOOPS """
text = "Python"
for character in text:
    print(character)

"""Looping through list"""

languages = [ "English","Nepali","Japnese"]
for language in languages:
    print(language)

""" Python main fucntion """
count = 1 

while  count <= 5:
    print(count)
    count = count + 1


for count in range(1, 6, 2):
    print(count)

num = int(input("Enter an integer:"))

for count in range(1, 11):
    product = num * count
    print(num ,"*", count,"=",product)
    

""" Can you create a program to find the sum of numbers from 1 to 100?"""
'''Result should be equal to :'''
''' result = 1+2+3+4+...+100'''

num = 0

for count in range(1,9):
    num = num + count
    print(num)

'''What we learned?'''
# Loops are used in programming to repeat a block of code
# A for loop is used to iterate through a sequence .
# If we know the number of iterations of the loop, it's easier and better to use the for loop.
# Range() is a useful function that create a sequence of numbers. It's common to use range() in a for loop to iterate the loop a certain number of times