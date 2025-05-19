# %% ===================================================================== #
#                                   ABOUT                                  #
# ======================================================================== #
# --------------------- Compiled by: (Dr.) B.C. Yadav -------------------- #
# ------------------------ On: 2025/03/26 18:03:35 ----------------------- #
# --------------------- Updated: 2025/05/19 19:12:48 --------------------- #
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



# %% ===================================================================== #
#                               SET DATA TYPE                              #
# ======================================================================== #



# %% ===================================================================== #
#                           DICTIONARY DATA TYPE                           #
# ======================================================================== #



# %% ===================================================================== #
#                                    END                                   #
# ======================================================================== #