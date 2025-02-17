'''Lists & Tuples in Python ''' # List are mutuable mean it can be changed

# a list of integers
numbers = [1, 2, 4, 5, 6]
print(numbers)
print(len(numbers))

#mixed list
random_list = [ 2.5, "Hello", -5, 2.5]
print(random_list)
print(len(random_list))

#empty list
list1 = []
print(len(list1))


''' Access the list order'''

languages = ["Python", "JavaScript", "C++","Kotlin"]
print(languages[0])
print(languages[3])
print(languages[-1])

''' Slicing of a list '''
names = ["ram","hari","shyam","krisha","Gaurab"]
print(names[0:])
print(names[1:3])

'''Change Items of a list'''
lan = ["Python", "Javascript", "C++", "Kotlin"]
lan[1:3] = ["Ruby", "Dart"]
print(lan)

''' Iterating through a list '''
print("Python" in lan)
print("Rust" in lan)

for lang in lan:
    print(lang)

'''List method'''
vasa = ["Nepali", "Chinese", "Indian", "Russian"]
vasa.insert(1,"American")
vasa.remove("Nepali")
print(vasa)
vasa1 = vasa.copy()
print(vasa1)


""" Tuples -->> Immutables mean cannot be changed"""
numbers = (21, -4, 54)
print(numbers[1])

bu = (1, 3, 5, 3, 2, 1)
for bue in bu:
    print(bu)

mixed_list = ["Hello", -34, "Java", True]

print("1.", mixed_list[-1])

mixed_list[1] = "Hi"
print("2.", mixed_list)


'''What we learned?'''
# A list is a collection of ordered items.
# To access individual elements of a list, we use indicies.
# To access a portion of a list, we use the slicing operator.
# Python has several useful methods that make it easier to add, change, insert and remove list elements.
# a tuple is similar to a list except tuples are immutable: we cannot change elements of a tuple.