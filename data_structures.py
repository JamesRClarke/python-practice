## Dictionaries
## These are what I know as objects but are known as dictionary in Python
# people = { 'Stuart': 28, 'James': 23 }
# print people['James']

# numbers = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five'
# }
#
# print 1 in numbers # check value key 1 in numbers dictionary - True
# print 19 in numbers # check value key 1 in numbers dictionary - False
#
# ## .get()
# print numbers.get(1) # get the key's value
# print numbers.get(19, "Key not found") # second argument is returned if key isn't found


## Tuples
## These are what I know as constants and are immutable but for any data structure ?
# fruits = ("Apple", "Mango", "Peach") # Tupple is defined by paranthesese
# fruits = "Apple", "Mango", "Peach" # Tupplem can be defined with no paranthesese
#
# fruits[0] = "Banana" # will not work as a Tupple is immutable

## Generators
# def func():
#     counter = 0
#     while counter < 5:
#         yield counter
#         counter += 1
#
# for x in func():
#     print x
#
#
# def even_numbers(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i
#
# print list(even_numbers(21))




## ARRAY / LISTS
# numbers = [1, 2, 3, 4, 5]
# numbers[1] = 1.5
# print numbers
#
# newnumbers = [2, 3, 3, 3, 3]
# print numbers + newnumbers # join two arrays together
#
# print numbers * 3 # print array 3 times as one array
#
# fruits = ["apple", "banana", 'pear']
#
# # in - checks array for match of given item and returns Boolean
# print "apple" in fruits # returns boolean: True
# print "orange" in fruits # returns boolean: False
#
# # .append - adds new item into end of array
# fruits.append("orange")
# print fruits
#
# # .len - shows number of items in array
# print len(fruits)
#
# # .insert - inserts item into position specifed to the array
# fruits.insert(1, "Mango")
# print fruits
#
# # .index - specifies the index of a given item
# print fruits.index("pear")
#
# # Range
# # list() generates an array of given input
# numbers = list(range(10))
# print numbers # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# numbers = list(range(3 , 8))
# print numbers # [3, 4, 5, 6, 7, 8]
#
# numbers = list(range(1 , 30, 3)) # 3rd argument creates an interval of given item
# print numbers # [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]

## Slicing
## the colon is used as a `slice`
# numbers = [0, 100, 200, 300, 400, 500, 600]
#
# print numbers[2:5] # [200, 300, 400]
# print numbers[:4] # [0, 100, 200, 300]
# print numbers[1:6:2] # the second colon defines an interval # [100, 300, 500]

## Comprehensions
## apply logic to define a list
# list = [x ** 2 for x in range(5)] # create a rule to define a list # [0, 1, 4, 9, 16]
# print list

## define only even list of numbers
# list = [x ** 2 for x in range(10) if x**2 % 2 == 0 ] # [0, 4, 16, 36, 64]
# print list

# def add(x):
#     return x + 2
#
# newlist = [10,20,30,40,50]
#
# result = list(map(add, newlist)) # [12, 22, 32, 42, 52]
# print result
#
# lambdaresult = list(map(lambda x: x + 2, newlist)) # [12, 22, 32, 42, 52]
# print lambdaresult

# newlist = [1, 3, 4, 5, 7, 2, 9, 11, 13]
#
# result = list(filter(lambda x: x % 2 == 0, newlist))
# print result




## Strings

## String formatting
## the .format function pass in the values you want to display inside a string
# numbers = [8,  5,  2020]
# newstring = "Date: {0}/{1}/{2}".format(numbers[0], numbers[1], numbers[2])
# print newstring
#
# a = '{x}/{y}'.format(x = 100, y = 200)
# print a

## .join is used to join items in a list
# print ', '.join(["Apple", "Banana", "Mango"]) # Apple, Banana, Mango
#
# ## .replace is used to replace given input with second argument
# print 'Hello there'.replace("there", "James") # Hello James
#
# ## .startswith & .endswith .lower - self-documenting
# newstring = "This is a string"
# print newstring.startswith("This") # True
# print newstring.endswith("string") # True
# print newstring.lower() # this is a string
#
#
# ## Numbers
# print min(1,2,3,4,5) # 1
# print max(1,2,3,4,5) # 5
#
# ## abs() always returns the absolute number i.e. always posotive
# print abs(-203) # 203
