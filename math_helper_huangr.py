import math

#choice = float(input("Which formula would you like to use?"))

def pythagtheo(a,b,c):
    '''when given 2 sides of a right triangle, returns missing side
    >>> pythagtheo(3,4,0)
    5.0
    >>> pythagtheo(0,4,5)
    3.0
    >>> pythagtheo(3,0,5)
    4.0
    
    
    The hypotenuse cannot equal either of the side lengths
    >>> pythagtheo(30,0,30)
    Traceback (most recent call last):
        ...
    ValueError: c cannot equal a or b
    
    There are no negative lengths
    >>> pythagtheo(-3,4,0)
    Traceback (most recent call last):
        ...
    ValueError: a,b,and c must be positive
    
    '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("a,b,and c must be positive")
    
    if c == a or c == b:
        raise ValueError("c cannot equal a or b")
    
    if a == 0:
        return math.sqrt(c**2-b**2)
    elif b == 0:
        return math.sqrt(c**2-a**2)
    else:
        return math.sqrt(a**2+b**2)
    
def herons(a,b,c):
    '''when given 3 sides of a triangle, returns area using semiperimeter
    >>> herons(3,4,5)
    6.0
    
    >>> herons(5,12,13)
    30.0
    
    >>> herons(8,15,17)
    60.0
    
    A triangle can't have a side with length of 0
    >>> herons(0,5,5)
    Traceback (most recent call last):
        ...
    ValueError: a,b,or c cannot equal 0
    
    There are no negative lengths
    >>> herons(-3,4,5)
    Traceback (most recent call last):
        ...
    ValueError: a,b,and c must be positive
    
    Triangle Inequality Theorem:
    >>> herons(3,4,10)
    Traceback (most recent call last):
        ...
    ValueError: a,b,and c must be able to form a triangle
    '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("a,b,and c must be positive")
    
    if a == 0 or b == 0 or c == 0:
        raise ValueError("a,b,or c cannot equal 0")
    
    if not(a+b>c and c+b>a and c+a>b):
        raise ValueError("a,b,and c must be able to form a triangle")
    
    semi = (a + b + c)/2
    return math.sqrt(semi*(semi-a)*(semi-b)*(semi-c))
                        
def sasarea(a,b,C):
    '''when given 2 adjacent side lengths and the angle between the 2 of a triangle, returns the area of the triangle

    >>> sasarea(3,4,90)
    6.0
    
    >>> sasarea(8,15,90)
    30.0
    '''
    if C == math.radians(C):
        return (a*b*math.sin(C))/2
    else:
        return (a*b*math.sin(math.radians(C))/2)
    
                         
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #main()