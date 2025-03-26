# %% ===================================================================== #
#                                   ABOUT                                  #
# ======================================================================== #
# --------------------- Compiled by: (Dr.) B.C. Yadav -------------------- #
# ------------------------ On: 2025/02/20 05:12:10 ----------------------- #
# --------------------- Updated: 2025/03/26 17:57:30 --------------------- #
# ======================================================================== #
# This code demonstrates parts of the Python concepts needed to code efficiently, focussing on operators.



# %% ===================================================================== #
#                                BACKGROUND                                #
# ======================================================================== #
# Types of operators in python 

# | Operators               | Type                      |
# |-------------------------|---------------------------|
# | +, -, *, /, %           | Arithmetic operator       |
# | <, <=, >, >=, ==, !=    | Relational operator       |
# | AND, OR, NOT            | Logical operator          |
# | &, \|, <<, >>, ~, ^     | Bitwise operator          |
# | =, +=, -=, *=, %=       | Assignment operator       |
# | is, is not              | Identity operator         |
# | in, not in              | Identity operator         |
# | Operator Precedence & Associativity |               |



# %% ===================================================================== #
#                           ARITHMETIC OPERATORS                           #
# ======================================================================== #
a, b = 15,7

# Addition, Subtraction, Multiplication and Division
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)

# Floor division - returns the quotient
print("\nFloor division:", a//b)

# Modulus - returns the remainder
print("Modulus:", a%b)

# Exponent
print("Exponent:", a**b)



# %% ===================================================================== #
#                           RELATIONAL OPERATORS                           #
# ======================================================================== #
# Relational operators compares the values and return either True or False according to the validity of the comparison.
a = 13
b = 33

print(f"Is {a} greater than {b}? {a > b}")
print(f"Is {a} less than {b}? {a < b}")
print(f"Is {a} equal to {b}? {a == b}")
print(f"Is {a} not equal to {b}? {a != b}")
print(f"Is {a} greater than or equal to {b}? {a >= b}")
print(f"Is {a} less than or equal to {b}? {a <= b}")



# %% ===================================================================== #
#                             LOGICAL OPERATORS                            #
# ======================================================================== #
# Logical operators execute operations such as Logical AND, Logical OR, and Logical NOT. They are utilized to combine conditional statements.
# The Logical NOT operator has the highest precedence, followed by the Logical AND operator, and finally, the Logical OR operator, which has the lowest precedence.

a = True
b = False
print(a and b)
print(a or b)
print(not a)



# %% ===================================================================== #
#                        BITWISE OPERATORS IN PYTHON                       #
# ======================================================================== #
# Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.
# Bitwise Operators in Python are as follows: Bitwise NOT, Bitwise Shift, Bitwise AND, Bitwise XOR and Bitwise OR.

a = 10  
b = 4   

print(a & b)   # Bitwise AND
print(a | b)   # Bitwise OR
print(~a)      # Bitwise NOT
print(a ^ b)   # Bitwise XOR
print(a >> 2)  # Right shift (divide by 4)
print(a << 2)  # Left shift (multiply by 4)



# %% ===================================================================== #
#                      ASSIGNMENT OPERATORS IN PYTHON                      #
# ======================================================================== #
# Python Assignment operators are used to assign values to the variables. This operator is used to assign the value of the right side of the expression to the left side operand.
a = 10
b = a  # assign a to b
print(b)

b += a  # add a to b
print(b)

b -= a  # add (-a) to b
print(b)

b *= a  # multiply b by a
print(b)

b <<= a  # left shift by by a
print(b)



# %% ===================================================================== #
#                            IDENTITY OPERATORS                            #
# ======================================================================== #
# `is` and `is not` are the identity operators both used to check if two values are located on the same part of the memory. They evaluate to True if the two operands are the same object, and False otherwise.
# Its worth noting that if two variables that are equal (a==b) do not imply that they are identical (a is b).


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")  # values are equal
print(f"a is b: {a is b}")  # different objects in memory
print(f"\na is c: {a is c}")  # a and c refer to the same object
print(f"a is not c: {a is not c}")



# %% ===================================================================== #
#                           MEMBERSHIP OPERATORS                           #
# ======================================================================== #
# The `in` and `not in` operators in Python are used to test whether a value or variable is present in a sequence (such as a list, tuple, string, or set). 
# They evaluate to True if the value is found in the sequence, and False otherwise.

numbers = [1, 2, 3, 4, 5]

print(f"5 in numbers: {5 in numbers}") 
print(f"5 not in numbers: {5 not in numbers}") 
print(f"\n10 in numbers: {10 in numbers}") 
print(f"10 not in numbers: {10 not in numbers}") 



# %% ===================================================================== #
#                             TERNARY OPERATOR                             #
# ======================================================================== #
# Ternary operators or conditional expressions, are operators that evaluate something based on a condition being true or false. 
# They allow testing a condition in a single line, replacing the multi-line if-else, making the code more compact.

# Assignment
a, b = 10, 20
min = a if a < b else b
print(min)

# Nested ternary operator
age = 7
is_adult = "Adult" if age >= 18 else "Minor" if age >= 13 else "Child" if age>=5 else "Kid"
print(is_adult)  

# In a function
def is_even(num):
    return "Even" if num % 2 == 0 else "Odd"
number = 7
result = is_even(number)
print(result)  



# %% ===================================================================== #
#                                    END                                   #
# ======================================================================== #