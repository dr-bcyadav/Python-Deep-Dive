# %% ===================================================================== #
#                                   ABOUT                                  #
# ======================================================================== #
# --------------------- Compiled by: (Dr.) B.C. Yadav -------------------- #
# ------------------------ On: 2025/01/06 19:48:02 ----------------------- #
# --------------------- Updated: 2025/02/14 14:11:43 --------------------- #
# ======================================================================== #
# This code covers part of the Python concepts needed to code efficiently, focussing on python naming convention, multiple assignment of variables, etc.



# %% ===================================================================== #
#                                 LIBRARIES                                #
# ======================================================================== #
import pandas as pd 
import keyword



# %% ===================================================================== #
#                      COMMENTS AND NAMING CONVENTION                      #
# ======================================================================== #
# Python ignores the string literals left unassigned to any variable, which can then be used as comments as follows: 
"""So, we can use these string literals as comments, or the usual hash preceded statements."""

# Variables and functions in python are named in the convention of snake case while classes are named in Pascal case respectively.
# snake case refers to all lowercase words separated by underscore
# Pascal case refers to all words starting with a capital letter.



# %% ===================================================================== #
#                     MULTIPLE ASSIGNMENT OF VARIABLES                     #
# ======================================================================== #
# Assigning same value to multiple variables
a = b = c = 100
print(a,b,c)

# Assigning different values to multiple variables 
a,b,c = 1,2.5,'this_string'
print(a,b,c)

# Practical example of swapping two variables 
a, b = 5, 10
a, b = b, a
print(a, b)



# %% ===================================================================== #
#                        LOCAL AND GLOBAL VARIABLES                        #
# ======================================================================== #
def f():
    a = "local variable"
    print(a)

# Accessing it globally will raise error 
print(a)

# Global variable on the other hand are versatile
def g():
    global b
    b = "global variable"
    print(b)

print(b)
# - Note that while declaring a global variable inside a function, the statement declaring it to be global is essential, before defining its value.



# %% ===================================================================== #
#                       OBJECT REFERENCING IN PYTHON                       #
# ======================================================================== #
# Let us assign a variable x to a value 5
x = 5

#        x
#        ↓
#        ↓
# +-------+
# |       |
# |   5   |
# |       |
# +-------+

# When x = 5 is executed, Python creates an object to represent the value 5 and makes x reference this object.

# Now, if we assign another variable y to the variable x.
y = x

#        x
#        ↓
#        ↓
# +-------+ ← ← y
# |       |
# |   5   |
# |       |
# +-------+

# When Python encounters the first statement (x=5), it creates an object for the value 5 and makes x reference it. The second statement (y=x) creates y and references the same object as x, not x itself. This is called a Shared Reference, where multiple variables reference the same object.

# Now if we write x = 'bcy'
x = 'bcy'

# Python creates a new object for the value "bcy" and makes x reference this new object. The variable y remains unchanged, still referencing the original object 5.

#         x           y  
#         ↓           ↓
#         ↓           ↓
# +-------+   +-------+
# |       |   |       |
# |  bcy  |   |   5   |
# |       |   |       |
# +-------+   +-------+

# If we now assign a new value to y:
y = 'git'

# Python creates yet another object for 'git' and updates y to reference it. The original object 5 no longer has any references and becomes eligible for garbage collection.

#         x                       y
#         ↓                       ↓
#         ↓                       ↓
# +-------+   +-------+   +-------+
# |       |   |       |   |       |
# |   bcy |   |   5   |   |   git |
# |       |   |       |   |       |
# +-------+   +-------+   +-------+

# We can always delete a variable in python using the `del` keyword. Trying to access a variable deleted from the namespace or an undefined one, both raise `NameError`
x = 10
del x 
# print(x)  # deleted variable

# print(z)  # undefined variable



# %% ===================================================================== #
#                                    END                                   #
# ======================================================================== #