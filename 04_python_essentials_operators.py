# %% ===================================================================== #
#                                   ABOUT                                  #
# ======================================================================== #
# --------------------- Compiled by: (Dr.) B.C. Yadav -------------------- #
# ------------------------ On: 2025/02/20 05:12:10 ----------------------- #
# --------------------- Updated: 2025/02/25 15:48:48 --------------------- #
# ======================================================================== #
# This code demonstrates parts of the Python concepts needed to code efficiently, focussing on operators.



# %% ===================================================================== #
#                                BACKGROUND                                #
# ======================================================================== #
# Types of operators in python 

# | Operators             | Type                    |
# |-----------------------|-------------------------|
# | +, -, *, /, %         | Arithmetic operator     |
# | <, <=, >, >=, ==, !=  | Relational operator     |
# | AND, OR, NOT          | Logical operator        |
# | &, \|, <<, >>, ~, ^   | Bitwise operator        |
# | =, +=, -=, *=, %=     | Assignment operator     |



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
# Add operators from this point beyond to toc