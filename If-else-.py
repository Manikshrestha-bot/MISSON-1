'''If...else Statement '''

# Suppose you are a university student and to pass the examination you need to score 50 or more. If your score is 50 or more, Print"YOU have passed your exams".

# score = int(input("Enter your score:"))
# if score >= 50:
#     print("You have passed your exams")
#     print("Congratulations")

# if score < 50:
#     print("You are failled")


#     '''OR'''

# score = int(input("Enter you score:"))
# if score >= 30:
#     print("You are passed!")
# else:
#     print("You are failled! Sorry ")

'''If..elif..else'''

# score = int(input("Enter your score:"))

# if score > 100 or score <0: 
#     print("Score is invalid")
# elif score >= 50:
#     print("You have passed your exam.")
# else:
#     print("You are failled! Sorry ")


'''Task'''
# Create a program to check whether a number is positive or negative or 0. For this, create a variable named number & assign a float value to it based on the user input. Then using a if statement, check if the number variable is possitive or negative or 0.# 


# If number is positive, print"The number is positive"
# If number is negative, print"The number is negative"
# If number if 0, print " The number is 0"

number = float(input("Enter a number:"))

if number < 0:
    print("The number is negative")
elif number > 0:
    print("The number is positive")
else:
    print("The number is 0")


''' What we learned about if..elif...else'''
# The if statement is used to create programs that can make decisions.
# The if statement executes its body only when the test condition is true.
# The if statement can have an optional else clause.
# The body of else is executed if the test condition is false.
# To run a block of code among more than 2 alternatives, we can use elif clauses inside the if.