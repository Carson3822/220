import math


def quadratic(a, b, c):
    disc = b * b - 4 * a * c
    if disc < 0:
        print('no real roots')

    elif disc == 0:
        sqrt_discr = math.sqrt(disc)
        denom = 2 * a
        root_1 = (-b + sqrt_discr) / denom
        print('double root at:', root_1)

    else:
        sqrt_discr = math.sqrt(disc)
        denom = 2 * a
        root_1 = (-b + sqrt_discr) / denom
        root_2 = (-b - sqrt_discr) / denom
        print("root 1:", root_1, "root 2:", root_2)



# if statement are alone need to be followed by elif or else, each if statment unless nested is own thing


# can test multiple things using and operator
# and returns a true or a false just like other boolean operators ( >, <, <=, >=, == )
# < bool and bool > returns boolean
# if x > 3 and x < 10 and x == 7:
# is x > 3 and x < 10

#find maximum value of 3 inputs

def max_val(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

#works but as we add values to check the logic gets long and complicated
def max_val_v2(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    elif b >= c:
        return b
    return c


def max_val_v3(a, b, c):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c

    return max_value


def max_val_v4(values):
    max_value = values[0]
    for value in values:
        if value >= max_value:
            max_value = value

    return max_value

max(1, 2, 3)