# """Break * Continue in loop"""
# for item in range(1,6):
#     if item == 3:
#         break
#     print(item)
# print("Break is applied on 3 before going on 4")


# for num in range(1, 12):
#     if num == 2:
#         continue
#     print(num)


# while True:
#     num = float(input("Enter a number:"))
#     if num < 0:
#         break
#     print("You entered:",num)


# for num in range(5):
#     number = float(input("Enter a number:"))
#     if number <0:
#         continue
#     print(number)

languages = ["Python", "Java", "Swift", "C", "C++"]

for language in languages:
    if language == "Java" or language == "Swift":
        continue
    print(language)


fruits = ["Apple", "Banana","Mango"]
for fruit in fruits:
    if fruit == "Apple" or fruit == "Mango":
        continue
    print(fruit)

'''What we learned?'''
# The break statement terminates the loop immediately when it is encountered.
# The continue statement skips the code after it for that iteration of the loop.
# The break & continue statements are almost always used inside the if...else statement.


'''Pass statement'''
num = 5.5

if num > 0.0:
    pass

''' What we learned? '''
# In python, pass is a null statement that does nothing.
# The pass statement is used to create loops, if...else statement, functions & classes with an empty body.