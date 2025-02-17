'''Class & Object'''
class Student:
    pass

# When working with objects, variables are called attributes and functions are called methods.

student1 = Student()
student1.name = "Manik"
student1.marks = 74

print(student1.name)
print(student1.marks)


class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

student1 = Student()
student1.name = "Manik"
student1.roll = 17
student1.marks = 73


did_pass = student1.check_pass_fail()
print(did_pass)

student2 = Student()
student2.name = "Anoj"
student2.roll = 16
student2.marks = 22

did_pass = student2.check_pass_fail()
print(did_pass)


""" The init method """
# The init method is a special method that automatically gets called everytime objects are created.


class Students:
    def check_pass_fail(self):
        if self.marks >= 30:
            return True
        else:
            return False
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student1 = Students("Hari", 89)
student2 = Students("Shyam", 21)

did_pass = student1.check_pass_fail()
print(did_pass)
did_pass = student2.check_pass_fail()
print(did_pass)



class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)
        return result

n1 = Complex(5, 6)
n2 = complex(-4, 2)
result = n1.add(n2)
print("real=",result.real )
print("imag =",result.imag)

#Defining a class
class Car:
    def __init__(self, brand, color):
        self.brand = brand    #Property (attrinute) ---> self.brand
        self.color = color    #Property (attribute)  ---> self.color

    def show_info(self):
        print(f"This car is a {self.color} {self.brand}")

# Creating a objects (instances of the class )
car01 = Car("Honda","REd")
car02 = Car("Toyota","Black")


car01.show_info()   # Output: This car is a REd Honda
car02.show_info()   # Output: This car is a Black Toyota



"""SUMMARY"""
# Car is the class(blueprint).
# car01 & car02 are objects created from that class.
# Each object has its own brand and color.
# show_info() is a method that prints the car's details.


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"The name of the student is {self.name}.His/Her age is {self.age} and His/Her grade is {self.grade}")


student01 = Student("Ram",12,"A")
student02 = Student("Shyam",13,"A+")

student01.display_info()
student02.display_info()



class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.s = a + b + c

    def calculate(self):
        print(f"The perimeter of the triangle is {self.s}.")

triangle1 = Triangle(22, 22, 22)

triangle1.calculate()


#Rule:
# ✅ We mention parameters in __init__ only if we need input from the user.
# ✅ If something can be calculated inside the class, we don't ask the user for it.



class BankAccout:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    '''account_holder stores the name of the person (e.g., John).
       balance stores the initial amount of money (we give it a default value of 0 if not provided).
       self is how the class refers to itself. It’s like saying, "I am the object, and these are my attributes." '''

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing ${amount}...New balance:${self.balance}")


        '''  deposit is the method to add money to the balance.
             self.balance means the balance of the specific bank account (the one that called this method).
             amount is how much money we want to add.  '''

    def withdraw(self, amount):
         if self.balance >= amount:
             self.balance -= amount
             print(f"Withdrawing ${amount}.. New balance:${self.balance}")
         else:
             print("Insufficient balance!")


    '''  withdraw is the method to take money out of the account.
    We check if the balance is enough to cover the amount they want to withdraw.
    If there’s enough, we subtract the amount from the balance. If not, we show an error.  '''


    def display_balance(self):
        print(f"Current balance: ${self.balance}")


    ''' display_balance simply prints the current amount in the account. '''



account1 = BankAccout("Honey",500)

''' This creates a new account for "John" with an initial balance of $500. '''



print(f"Welcome {account1.account_holder}!")
print("\nDepositing $200..")
account1.display_balance()   # shows the current balance

print("\nDepositing $200..")
account1.deposit(200)        # Deposits $200 into the account


print("\nWithdrawing $100")
account1.withdraw(100)       # Withdraws $100 from the account

print("\nWithdrawing $800..")
account1.withdraw(800)       # Tries to withdraw more than available balance (will show an error)


