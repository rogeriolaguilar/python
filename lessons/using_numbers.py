# scientific notation
print(5e32)
print(999999999999999999999999999999999.9)

# Infinity
print(1e499)
print(1e500)
print(-1e500)

# Conversions
print(float(4)) # 4.0
print(int(3.4)) # 3
print(int(-3.4)) # -3

# arithimetic
print(3 + 6.7)
print(3 * 4.1) # 12.299999999...
print(8 / 2) # 4.0
print(8 // 2) # 4
print(7.81 / 12.4) # 0.629.....
print(7.81 // 12.4) # 0
print( 3 ** 2) # 9


"""
Demonstration of compound arithmetic expressions in Python
"""

# Expressions can include multiple operations
print("Compound expressions")
print(3 + 5 + 7 + 27)
print(18 - 6 + 4)

print("")

# Operator precedence defines how expressions are evaluated
print("Operator precedence")
print(7 + 3 * 5) # 22
print(5.5 * 6 // 2 + 8) # 24.0

print(-3 ** 2) # -9
print((-3) ** 2) # 9


# Use parentheses to change evaluation order
print("Grouping with parentheses")
print((7 + 3) * 5)
print(5.5 * ((6 // 2) + 8))
print((-3) ** 2)

