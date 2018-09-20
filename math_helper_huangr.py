import math
import time
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
    
    A triangle can't have a side with length of 0 or less
    >>> pythagtheo(-3,0,0)
    Traceback (most recent call last):
        ...
    ValueError: a,b,and c must be greater than 0
    
    '''
    
    if (a < 0 or b < 0 or c < 0) or (a+b)==0 or (b+c)==0 or (a+c)==0:
        raise ValueError("a,b,and c must be greater than 0")
    
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
    
    A triangle can't have a side with length of 0 or less
    >>> herons(0,5,-5)
    Traceback (most recent call last):
        ...
    ValueError: a,b,and c must be greater than 0
    
    Triangle Inequality Theorem:
    >>> herons(3,4,10)
    Traceback (most recent call last):
        ...
    ValueError: a,b,and c must be able to form a triangle
    '''
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("a,b,and c must be greater than 0")
    
    if not(a+b>c and c+b>a and c+a>b):
        raise ValueError("a,b,and c must be able to form a triangle")
    
    semi = (a + b + c)/2
    return math.sqrt(semi*(semi-a)*(semi-b)*(semi-c))
                        
def sasarea(a,b,C):
    '''when given 2 adjacent side lengths and the angle between the 2 of a triangle, returns the area of the triangle

    >>> sasarea(3,4,90)
    6.0
    
    >>> sasarea(8,15,90)
    60.0
    
    >>> sasarea(5,12,90)
    30.0
    
    Sum of interior angles of a triangle equal 180 degrees
    >>> sasarea(3,4,180)
    Traceback (most recent call last):
        ...
    ValueError: C must be less than 180 degrees
    
    A triangle can't have a side length nor degree measure of less than or equal to 0
    >>> sasarea(0,5,-9)
    Traceback (most recent call last):
        ...
    ValueError: a,b,or C must be greater than 0
      
    
    '''
    if a <= 0 or b <= 0 or C <= 0:
        raise ValueError("a,b,or C must be greater than 0")
    if C >= 180:
        raise ValueError("C must be less than 180 degrees")
    
    if C == math.radians(C):
        return (a*b*math.sin(C))/2
    else:
        return (a*b*math.sin(math.radians(C)))/2

def pointslope(x1,y1,x2,y2):
    '''when given 2 points , finds the point slope form of the line created by those 2 points

    >>> pointslope(1,0,2,0)
    y-0=0.0(x-1)
    
    >>> pointslope(1,1,2,2)
    y-1=1.0(x-1)
    
    >>> pointslope(900,3,2003,4)
    y-3=0.0009066183136899365(x-900)
    
    >>> pointslope(0,0,0,9)
    Too bad. Slope is undefined. x=0
    
    >>> pointslope(0,0,0,0)
    Traceback (most recent call last):
        ...
    ValueError: You must input 2 DIFFERENT points
    
    

    '''
    if x1 == x2 and y1 ==y2:
        raise ValueError("You must input 2 DIFFERENT points")
    
    if (x2-x1)==0:
        print(f"Too bad. Slope is undefined. x={x1}")

    else:
        slope = (y2-y1)/(x2-x1)
        print(f"y-{y1}={slope}(x-{x1})")


    
def perpbisector(x1,y1,x2,y2):
#handle y--y1 error
    '''when given 2 points, finds the point slope form of the line that bisects the line segment created by those 2 points and is perpendicular to that line segment

    >>> perpbisector(1,9,45,23)
    y-23.0=-3.142857142857143(x-16.0)

    >>> perpbisector(23,-443,53,10)
    y-38.0=-0.06622516556291391(x--216.5)
    
    >>> perpbisector(2,34,12,414234)
    y-7.0=-2.4142926122646064e-05(x-207134.0)
    
    >>> perpbisector(3,0,2,0)
    x = 2.5
    
    >>> perpbisector(0,3,0,2)
    y = 2.5
    
    >>> perpbisector(0,0,0,0,)
    Traceback (most recent call last):
        ...
    ValueError: You must input 2 DIFFERENT points
    
    '''
    if x1 == x2 and y1 ==y2:
        raise ValueError("You must input 2 DIFFERENT points")
    
    x = (x1+x2)/2
    y = (y1+y2)/2
    if (y2-y1)==0:
        print(f"x = {x}")
    elif (x1-x2)==0:
        print(f"y = {y}")
    else:

        slope = -((y2-y1)/(x2-x1))**-1
        print(f"y-{x}={slope}(x-{y})")
    
def use_pythagtheo():
    print("Enter in 0 for the missing leg of the triangle")
    a = float(input("What is the length of one leg of the triangle:"))
    b = float(input("What is the length of the other leg of the triangle:"))
    c = float(input("What is the length of the hypotenuse of the triangle:"))
    print(f"The missing length:{pythagtheo(a,b,c)}")
    time.sleep(5)
    
def use_herons():
    a = float(input("What is the length of one leg of the triangle:"))
    b = float(input("What is the length of the other leg of the triangle:"))
    c = float(input("What is the length of the last leg hypotenuse of the triangle:"))
    print(f"The area is:{herons(a,b,c)}")
    time.sleep(5)
    
        
def main():
    while True:
        choice = (input('''Which formula would you like to use?
    (a) Pythagorean Theorem
    (b) Heron's Formula
    (c) Area of a triangle using SAS
    (d) Point slope form of line created by 2 points
    (e) Perpendicular Bisector of line created by 2 points
    '''))
        if choice == 'a':
            use_pythagtheo()
        elif choice == 'b':
            use_herons()

        
    
    
                         
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()