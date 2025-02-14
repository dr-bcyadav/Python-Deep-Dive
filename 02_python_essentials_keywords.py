# %% ===================================================================== #
#                                   ABOUT                                  #
# ======================================================================== #
# --------------------- Compiled by: (Dr.) B.C. Yadav -------------------- #
# ------------------------ On: 2025/01/06 19:48:02 ----------------------- #
# --------------------- Updated: 2025/02/14 14:11:43 --------------------- #
# ======================================================================== #
# This code covers part of the Python concepts needed to code efficiently, focussing on keywords.

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
# |Structure              |def, return, lambda, yield, class              |
# |Context Management     |with, as                                       |
# |Import and Module      |import, from, as                               |
# |Scope and Namespace    |global, nonlocal                               |
# |Async Programming      |async, await                                   |



# %% ===================================================================== #
#                                 LIBRARIES                                #
# ======================================================================== #
import pandas as pd 
import keyword



# %% ===================================================================== #
#                              VALUE KEYWORDS                              #
# ======================================================================== #
# True, False represent boolean values while Null is a special constant used to denote a null value or void.
print(False == 0)
print(True == 1)

print(True + True + True + True)
print(False + False + False + False)

# Null does not equate to zero or any empty data structure
print(None==0)
print(None==[])

# del is used to delete a reference to an object
str1 = "a string for use"
del str1



# %% ===================================================================== #
#                             OPERATOR KEYWORDS                            #
# ======================================================================== #
# ============================ And, Or And Not =========================== #
a, b = True, False
print(a and b)  # True when both true 
print(a or b)  # True when one of them is true 
print(not a)  # prints the negation of a



# %% ============================ In And Is ============================== #
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



# %% ===================================================================== #
#                           CONTROL FLOW KEYWORDS                          #
# ======================================================================== #
# ============================= If Elif Else ============================= #
# if elif else: An expression when true passes the control to `if` block, otherwise to the `elif` or `else` block.
if 4 > 5:
    print("This way")
elif 4 < 3:
    print("That way")
else:
    print("No way!")
    
# for keyword is used to create loop
for i in range(2):
    print('consistency')

# while keyword is used to create loop
i=0
while (i<2):
    print('consistency is the word')
    i+=1



# %% ======================= Break Continue Pass ========================= #
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

# pass keyword: pass is the null statement in python. It can be used as placeholder when code is to added later. 
n = 5
for i in range(n):
    if i==3:
        pass
    print(i)
# - Here above when i reaches 3, pass statement is executed which just does nothing and the execution is forwarded to the next line `print(i)` so 3 would still be printed.
    
# In the following example we replace `pass` with `continue` so when `i` reaches 3, the loop exits the current iteration and reaches the beginning of the next iteration. Nothing will be printed at `i==3` 
n = 5
for i in range(n):
    if i==3:
        continue
    print(i)



# %% ======================= Try Except Finally ========================== #
# try and except: Code in try block is checked and executed, and if there is any type of error, except block is executed. 
# finally: No matter the result of the try block, the code under final keyword is always executed.
a,b = 4,0
try:
    k=a//b
    print(k)
except:
    print('Seems like a zero division error.')
finally:
    print('This part of the code is always executed.')
    
    

# %% ======================== Assert And Raise =========================== #
# assert: Checks a condition, and if it’s False , raises an AssertionError. It works as: assert <condition>, "Optional error message if condition if false". It is generally used in debugging to catch unexpected situations/assumptions about the program
assert b!=0, "Divide by zero error"

# raise: It is used to explicitly raise an exception, and can be used to signal that an error has occurred and to propagate that error up the call stack. Unlike assertions, exceptions raised with raise are always active and will not be ignored.
tempString = 'Learning here'
if tempString!='here':
    raise TypeError('Strings are different')



# %% ===================================================================== #
#                            STRUCTURE KEYWORDS                            #
# ======================================================================== #
# ================================== Def ================================= #
# def is used to define a function
def PrintStatements():
    print('A print statement')    
PrintStatements()



# %% ============================== Class ================================ #
# class is used to define a user defined class. In the following example a class named 'Employee' is declared with two attributes.
class Employee():
    salary = 'Competitive'
    retention = 'yes'



# %% ========================= Return Vs Yield =========================== #
# return and yield: return provides a result from a function and exits immediately, while `yield` creates a generator and allows the function to yield multiple values without exiting the function.
def function_with_return():
    a=2
    return a

print(function_with_return())

def function_with_yield():
    yield 1
    yield 2
    yield 3

for value in function_with_yield():
    print(value)    
    


# ================================ Lambda ================================ #