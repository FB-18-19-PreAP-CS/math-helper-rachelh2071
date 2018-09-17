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
    
    a,b,or c can't be too large either
    >>> pythagtheo(1e100,0,4)
    Traceback (most recent call last):
        ...
    OverflowError: a,b,or c is too large
    '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("a,b,and c must be positive")
    
    if c == a or c == b:
        raise ValueError("c cannot equal a or b")
    
    if a+1 == a or b+1 == b or c+1 == c: 
        raise OverflowError("a,b,or c is too large")    
    
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
    
    '''
    semi = (a + b + c)/2
    return math.sqrt(semi*(semi-a)*(semi-b)*(semi-c))
                         

                         
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #main()