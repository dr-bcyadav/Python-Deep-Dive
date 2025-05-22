# %% ===================================================================== #
#                                   ABOUT                                  #
# ======================================================================== #
# --------------------- Compiled by: (Dr.) B.C. Yadav -------------------- #
# ------------------------ On: 2025/03/26 18:03:35 ----------------------- #
# --------------------- Updated: 2025/05/22 17:37:20 --------------------- #
# ======================================================================== #
# This code discusses about the various data types in python.



# %% ===================================================================== #
#                                  THEORY                                  #
# ======================================================================== #
# Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes. The following are the standard or built-in data types in Python: 
# Numeric – int, float, complex
# Sequence Type – string, list, tuple
# Boolean – bool
# Set Type – set, frozenset
# Mapping Type – dict




# %% ===================================================================== #
#                             NUMERIC DATA TYPE                            #
# ======================================================================== #
# Int, Float and Complex data types 
a = 10
print(type(a))

b = 10.5
print(type(b))

c = 3 + 5j
print(type(c))



# %% ===================================================================== #
#                            SEQUENCE DATA TYPE                            #
# ======================================================================== #
# Sequence data types are collection of similar or different data types. 



# %% ============================= Strings =============================== #
# Strings are arrays of bytes representing unicode characters. In python, there is no character datatype, rather, a character is a string of length 1.
# Strings in python can be created using single, double or even triple quotes.
# Different characters of a string can be accessed via indices.

msg = "Python is amazing"
print(type(msg))  

# Accessing string characters
print(msg[3]) 
print(msg[7]) 
print(msg[-1])



# %% ============================== Lists ================================ #
# Lists are just like arrays, declared in other languages which is an "ordered" collection of data. It is very flexible as the items in a list do not need to be of the same type.
# Lists in Python can be created by just placing the sequence inside the square brackets[].

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed int and string
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

# Indexing is 0-based and the last element has the index of -1
print(a[0])
print(a[1])
print(a[-1])



# %% ============================= Tuples ================================ #
# Just like a list, a tuple is also an ordered collection of Python objects of varying datatypes. The only difference between a tuple and a list is that tuples are immutable.
# The essential element that defines a tuple is the comma, not the parentheses.

example_tuple = (1, 2, 3)
example_tuple = 1, 2, 3

# - Parentheses are commonly used for readability and are required in certain cases such as empty tuples or single-element tuples.

# These are accessed in the same way as lists
print(example_tuple[0])
print(example_tuple[-1])



# %% ===================================================================== #
#                             BOOLEAN DATA TYPE                            #
# ======================================================================== #
# Python Data type with one of the two built-in values, True or False
print(type(True))
print(type(False))
print(type(true))  # error



# %% ===================================================================== #
#                               SET DATA TYPE                              #
# ======================================================================== #
# Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements, and can contain mixed data types.
# Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by a ‘comma’. 

# Initializing empty set
s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)

# Set items cannot be accessed by referring to an index since the sets are unordered and their items have no index. A workaround is using the 'in' keyword.
print("Geeks" in s2)



# %% ===================================================================== #
#                           DICTIONARY DATA TYPE                           #
# ======================================================================== #
# Dictionaries are made up of key-value pairs separated by commas. The values can be of any datatype and are repeatable while the keys can't be repeated and are immutable.

# Defining an empty one
d = {}

# Defining using curly braces
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# Defining using dict() constructor
d1 = dict({1: 'Geeks', 'two': 'For', 3: 'Geeks'})
print(d1)

# Elements can be accessed via keys either via square brackets or `.get()`
print(d1['two'])
print(d1.get('two'))



# %% ===================================================================== #
#                                    END                                   #
# ======================================================================== #