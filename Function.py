''' FUNCTIONS '''


def greet(name):
    print("Hello",name)
    return
    print("HOw do you do ?")

greet("Jack")


def add_num(n1, n2):
   result = n1 + n2
   print("The sum is", result)

num1 = 5
num2 = 5
add_num(num1, num2)

def add_num(n1, n2):
   result = n1 + n2
   return result

num1 = 5
num2 = 5
result = add_num(num1, num2)
print("The sum is", result)



marks = [ 55, 75, 75, 28, 84, 39]
print(len(marks))

marks = [ 55, 75, 58, 93]
length = len(marks)
print("Length is", length)

marks_sum = sum(marks)
print("The total marks you got is", marks_sum)


# function to find average marks

def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks

# calculate the grade and return it
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade



marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
print("YOur average marks is:", average_marks)

grade = compute_grade(average_marks)
print("Your grade is:", grade)


""" REPEAT """

def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks

def compute_grade(grade):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
print(average_marks)

grade = compute_grade(average_marks)
print("Your grade is", grade)


def add_numbers( num1, num2):
    return num1 + num2

def multiply_numbers( num1 , num2) :
    return num1 * num2

number1 = 5
number2 = 30

sum_result = add_numbers(number1, number2)
print( "Sum is", sum_result)
product_result = multiply_numbers(number1,number2)
print("Multiply is", product_result)



'''Can you create a program to add and multipy two numbers? For this, create two functions add_numbers() and multiply_numbers(). These functions should compute the result and return them to the function call. And, the results should be printed from outside the function.'''
 

def add_numbers(num1, num2):
    return  num1 + num2

def multiply_numbers(num1, num2):
    return  num1 * num2


number1 = 50
number2 = 30
sum_result = add_numbers(number1, number2)
print("Sum is:", sum_result)

product_result = multiply_numbers(number1, number2)
print("Product is:", product_result)

'''What we learned?'''
# A function is a block of code that performs a specific task.
# We use the def keyword to define a function.
# To bring the function into action, we need to call the function. The same function can be called many times as we want.
# We can pass values to a function. These values passed to functions are called arguments or parameters.
# The return statement can be used inside a function. It returns a value from a function & exits the function.