
def miles_to_feet(miles):
  feet_in_a_mile = 5280
  return feet_in_a_mile * miles
print(miles_to_feet(2))


import random
def powerball():
  n1 = random.randrange(1,60)
  n2 = random.randrange(1,60)
  n3 = random.randrange(1,60)
  n4 = random.randrange(1,60)
  n5 = random.randrange(1,60)
  n_power = random.randrange(1,36)
  print("Today's numbers are "+str(n1)+", "+str(n2)+", "+str(n3)+", "+str(n4)+", and "+str(n5)+". The Powerball number is "+ str(n_power)+ ".")
powerball()


def cube_root(val):
    """
    Given number, return the cube root of the number
    """
    return val ** (1 / 3)
print(cube_root(1.0))    



def project_to_distance(point_x, point_y, distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    print(point_x * scale, point_y * scale)

project_to_distance(2, 7, 4)




def do_stuff():
    """
    Example of print vs. return
    """
    print("Hello world")
    return "Is it over yet?"
    print("Goodbye cruel world!")

print(do_stuff())





def f(x):
  return (-5) * (x ** 5) + (67 * (x ** 2)) + 47
print(f(0))
print(f(1))
print(f(2))
print(f(3))




def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value * ( 1 + rate_per_period) ** periods
print("$1000 at 2% compounded daily for 4 years yields $", future_value(500, .04, 10, 10))
print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))


def equilateral_triangle_area(side_size):
    print(((3  ** 0.5) / 4) * side_size ** 2)
equilateral_triangle_area(2)
equilateral_triangle_area(5)    