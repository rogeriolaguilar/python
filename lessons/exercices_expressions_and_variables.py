"""
Practice Exercises for Expressions
"""
# There are 5280 feet in a mile. Write a Python statement that calculates and prints the number of feet in 13 miles. 
FEET_IN_A_MILE = 5280
print(13 * FEET_IN_A_MILE) # 69333332640

# Write a Python statement that calculates and prints the number of seconds in 7 hours, 21 minutes and 37 seconds.
SECONDS_PER_HOUR = 60 * 60
SECONDS_PER_MINUTE = 60
print(SECONDS_PER_HOUR * 7 + SECONDS_PER_MINUTE * 21 + 37) # 26497

#The perimeter of a rectangle is 2w+2h, where w and h are the lengths of its sides. Write a Python statement that calculates and prints the length in inches of the perimeter of a rectangle with sides of length 44 and 77 inches.
print( 2 * ( 4 + 7 ))

#The area of a circle is πr^2 where r is the radius of the circle. (The raised 2 in the formula is an exponent.) Write a Python statement that calculates and prints the area in square inches of a circle whose radius is 8 inches. Assume that the constant \pi = 3.14
print(3.14 * 8 ** 2) # 200.96


print("I'm " + str(27) + " years old.")

# Write a Python statement that calculates and prints the distance between the points (2, 2) and (5, 6). (Hint: Remember that a square root can be computed by raising a value to the 0.5 power.)
print(( (2-5)**2 + (2-6)**2 )**0.5) # 5.0

