# %% ===================================================================== #
#                                   ABOUT                                  #
# ======================================================================== #
# --------------------- Compiled by: (Dr.) B.C. Yadav -------------------- #
# ------------------------ On: 2025/03/26 18:03:35 ----------------------- #
# --------------------- Updated: 2025/03/26 18:03:35 --------------------- #
# ======================================================================== #
# This code discusses about the various data types in python.



# %% ===================================================================== #
#                                  THEORY                                  #
# ======================================================================== #
# Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes. The following are the standard or built-in data types in Python: 
# Numeric – int, float, complex
# Sequence Type – string, list, tuple
# Mapping Type – dict
# Boolean – bool
# Set Type – set, frozenset
# Binary Types – bytes, bytearray, memoryview




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