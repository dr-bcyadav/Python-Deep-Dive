# %% ===================================================================== #
#                                   ABOUT                                  #
# ======================================================================== #
# This code cover the essential concepts of Python to achieve high efficiency in coding operations.



# %% ===================================================================== #
#                                 LIBRARIES                                #
# ======================================================================== #
import pandas as pd 



# %% ===================================================================== #
#                                 COMMENTS                                 #
# ======================================================================== #
# Note: Python ignores the string literals that are not assigned to a variable. 
"""So, we can use these string literals as comments, or the usual hash preceded statements."""



# %% ===================================================================== #
#                     MULTIPLE ASSIGNMENT OF VARIABLES                     #
# ======================================================================== #
# Assigning same value to multiple variables
a = b = c = 100
print(a,b,c)

# Assigning different values to multiple variables 
a,b,c = 1,2.5,'this_string'
print(a,b,c)



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


