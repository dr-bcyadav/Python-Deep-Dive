# %% ===================================================================== #
#                                   ABOUT                                  #
# ======================================================================== #
# --------------------- Compiled by: (Dr.) B.C. Yadav -------------------- #
# ------------------------ On: 2025/01/06 19:48:02 ----------------------- #
# --------------------- Updated: 2025/01/06 19:48:02 --------------------- #
# ======================================================================== #
# This code cover the essential concepts of Python to achieve a good efficiency in coding operations.

# TOC:
    # Libraries
    # Comments
    # Multiple assignment of variables
    # Local and global variables 
    # Object reference in python
    # Keywords in python



# %% ===================================================================== #
#                                 LIBRARIES                                #
# ======================================================================== #
import pandas as pd 
import keyword



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
#                        OBJECT REFERENCE IN PYTHON                        #
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
#                            KEYWORDS IN PYTHON                            #
# ======================================================================== #
# Printing all keywords at once using "kwlist()"
for word in keyword.kwlist:
    print(word)

# - Most of the IDEs color the keywords distinctly. Above keywords can be categorized as follows: 

# |---------------------  |-----------------------------------------------|
# |Category               |Keywords                                       |
# |---------------------  |-----------------------------------------------|
# |Value Keywords         |True, False, None, del                         |
# |Operator Keywords      |and, or, not, in, is                           |
# |Control Flow Keywords  |if, else, elif, for, while, break, continue, pass, try, except, finally, raise, assert                                 |
# |Function and Class     |def, return, lambda, yield, class              |
# |Context Management     |with, as                                       |
# |Import and Module      |import, from, as                               |
# |Scope and Namespace    |global, nonlocal                               |
# |Async Programming      |async, await                                   |



# %% ========================= Value Keywords ============================ #
# True, False represent boolean values while Null is a special constant used to denote a null value or void.
print(False == 0)
print(True == 1)

print(True + True + True + True)
print(False + False + False + False)

# Null does not equate to zero or any empty data structure
print(None==0)
print(None==[])



# %% ======================== Operator Keywords ========================== #
# and, or and not 
a, b = True, False
print(a and b)  # True when both true 
print(a or b)  # True when one of them is true 
print(not a)  # prints the negation of a

# in keyword (membership operator): checks a value in a sequence (list, tuple, string, etc.)
print('s' in 'this code repository')

# is keyword: checks whether two variables point to the same object in memory 
# Example 1: 
print('2' is '2')

# Example 2:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # both point to same object
print(a is c)  # different objects (with same values)



# %% ====================== Control Flow Keywords ======================== #
# if elif else: An expression when true passes the control to `if` block, otherwise to the `elif` or `else` block.
if 4 > 5:
    print("This way")
elif 4 < 3:
    print("That way")
else:
    print("No way!")
    
# for and while are used to create loops
for i in range(2):
    print('consistency')

i=0
while (i<2):
    print('consistency is the word')
    i+=1
    
# break keyword is used to break out of the flow of a loop and pass the control to the next statement following immediately after the loop (e.g., an outer loop)
i=0
while i<4:
    i+=1
    if i==3:
        break
    print(i)

# continue keyword skips the current iteration of a loop and goes to its next iteration, and does not end the loop. 
i=0
while i<4:
    i+=1
    if i==3:
        continue
    print(i)

# pass keyword: pass is the null statement in python.


