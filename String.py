''' String '''
text = """ Hello there
HOw are you    oh ho ho 
Are you fine"""
print(text)


mess = "He said, \"What\'s there?\""
print(mess)

'''Accessing character in string'''
text = "PYTHON"
print(text[0])
print(text[3])
print(text[2])
print(text[-1])


'''Slicing a string'''

test = "tasty"
print(test[0:3])


'''Python String Operations'''

text1 = "Python"
text2 = "Programming"
result = text1 + text2
print(result)

text = "Manik"
new_text = text * 5
print(new_text)
for character in text:
    print(character)


print(len(text))


Book = "Chemistry"
print("mes" in Book )
print("mis" in Book)


text = " I like Python 4"
result = text.lower()
print(result)
result = text.upper()
print(result)


dayname ="Sunday Monday Tuesday Wednesday Thursday Friday Saturday"
name = dayname.replace("Monday", "Sunday")
print(name)

''' What we learned ?'''
# A string is a sequence of characters.
# To create a string, we can use either single quotes or double quotes or triple quotes.
# To access an individual character from a list, we use indices.
# T access a substring from a string, we use the slicing operator.
# A string is a sequence and we can iterate through characters of a string using a loop.
# There are several string methods that make it easy to work with strings.