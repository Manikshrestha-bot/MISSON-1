'''Dictionaries'''
person1 = {"name":"Manik", "age":18}
print(person1["name"])


person2 = {"name":"Hari", "age":21}
print(person2.get("hobbies",["Dancing","Singing"]))

person3 = {"name":"Rame", "age":22}
person3["name"] = "Amar"
print(person3.pop("name"))
print(person3)

'''Iterating through a dic '''
person4 = {"name":"Hari", "age":21}

for key in person4:
    print(key)
    print(person4[key])


""" What we learned? """
# A dictionary is a compound data type that allows us to work with key value pairs.
# We can easily access a value from a dictionary if it's key is known.
# To add/change items from a dictionary, we can assign values to the keys.
# We can remove items from a dictionary by using the pop() method.
# We learned to iterate through keys of a dictionary using a for loop.