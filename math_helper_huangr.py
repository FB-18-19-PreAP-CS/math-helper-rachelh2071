from math import *

choice = input("Which formula would you like to use?")   

def pythagtheo(a,b,c):
    '''when given 2 legs of a right triangle, returns length of hypotenuse'''
    if a == 0:
        return c**2-b**2
    elif b == 0:
        return c**2-a**2
    else:
        return a**2+b**2
