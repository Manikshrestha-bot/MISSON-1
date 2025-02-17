# numbers = [1, 4, 9, 16]
# print(type(numbers))


# n1 = 5 
# print(type(n1))


# flag = True 
# print(type(flag))


# def my_function():
#     pass

# print(type(my_function))


numbers_list = [1, 2]
# print(dir(numbers_list))

# result = numbers_list.__add__([3, 4])
result = numbers_list + [3, 4]
print(result)



"""    In Python, every object has an id for identity. The id of an object is always unique and constant for this object during its lifetime.   """
num1 = 5
print(id(num1))

num2 = 0
print(id(num2))

num3 =""
print(id(num3))

print(id(num1))
print(id(num2))
print(id(num3))


a = [1, 2, 3]
b = a.copy

a.append(4)

print("a=",a)
print("b=",b)
print(id(a))
print(id(b))