from math import *
#import doctest
#doctest.testmod()

#choice = float(input("Which formula would you like to use?"))

def pythagtheo(a,b,c):
    '''when given 2 sides of a right triangle, returns missing side
    '''
    if a == 0:
        return math.sqrt(c**2-b**2)
    elif b == 0:
        return math.sqrt(c**2-a**2)
    else:
        return math.sqrt(a**2+b**2)
    
def herons(a,b,c):
    '''when given 3 sides of a triangle, returns area using semiperimeter
    '''
    semi = (a + b + c)/2
    return math.sqrt(semi(semi-a)(semi-b)(semi-c))
