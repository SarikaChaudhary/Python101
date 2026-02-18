
""""
    Operators:
    1. Arithmetic Operators             + - / * %
    2. Relational Operators             < > <= >= == !=
    3. Logical Operators                and or not
    4. Bitwise Operators                 &  | ^ ~ << >>
    5. Assignment Operators             = += -= /= *= %=

"""

"""
    Python 3.x (Division Operator allows you to divide two numbers and return a quotient
    There are two types of divisions 
        1. float division
            Quotient returned by this operator is always a float no matter if two operands are integers
            5 / 5 = 1.0
            -10 / 5 = -2.0   
            
        2. Integer division (Floor Division)
            Quotient returned by the operator is dependent on the argument being passed
                if two operands are floats, returned value is a float
                if two operators are negative numbers, returned value will be floored (nearest lesser number)
            "//" operator is used to return the closed integer value which is less than or equal to a specified expression or value
            
            5 // 5 = 1
            3 // 2 = 1
            3 // 2.0 = 1.5
            -3 // 2 = -2 
            -5 // 2 = -3 
            
    Python 2.x
        x / y           `= (similar to)        x // y in Py 3.x
            
"""
def division_operator():
    a = 15
    b = 4

    # Float Division
    print("\nFloat Division Operator \n")
    print (f' 5 / 5 = ', 5 / 5)
    print (f' -10 / 5 = ', -10 / 5)
    print (f' 10.0 / 5 = ', 10.0 / 5)
    print (f' -10.0 / 5 = ', -10.0 / 5)

    # Integer division (floor division)
    print("\nFloor Division Operator \n")
    print(f' 5 // 5 = ', 5 // 5)
    print(f' -10 // 5 = ', -10 // 5)
    print(f' 10.0 // 5 = ', 10.0 // 5)
    print(f' -10.0 // 5 = ', -10.0 // 5)
    print(f' -3 // 2 = ', -3 // 2)
    print(f' -5 // 2 = ', -5 // 2) ## find the closest smaller number of -2.5 which is -3
    print(f' -5.0 // 2 = ', -5.0 // 2)   ## find the closest smaller number of -2.5 which is -3.0


def comparison_operator():
    a = 15
    b = 4
    print("\nComparison Operators \n")
    print(f' 15 > 4 = ', a > b)
    print(f' 15 < 4 = ', a < b)
    print(f' 15 == 4 = ', a == b)
    print(f' 15 != 4 = ', a != b)
    print(f' 15 >= 4 = ', a >= b)
    print(f' 15 <= 4 = ', a <= b)

    a = 3
    b = 3
    print(f' 3 == 3 = ', 3 == 3)
    print(f' 3 is 3 = ', a is b)

    b = 4
    print(f' 3 == 4 = ', 3 == 4)
    print(f' 3 is 4 = ', a is b)

    x = [10]
    a = x
    b = x
    print(f' {a} == {b} = ', a == b)  # True content of a and x are the same
    print(f' {a} is {b} = ', a is b) # False both are referencing the same object

    x = [10]
    a = x
    y = [10]
    b = y
    print(f' {a} == {b} = ', a == b) #True
    print(f' {a} is {b} = ', a is b) # False because list x is different from list y
    print(f' {a} is {b} = ', b == y) #True
    print(f' {a} is {y} = ', x is y) # False

    x = [10]
    a = x
    b = [10]
    print(f' {a} == {b} = ', a == b) # True
    print(f' {a} is {b} = ', a is b) # False



def logical_operator():
    print("\nLogical Operators \n")
    a = True
    b = False
    print(a and b)
    print(a or b)
    print(not a)

def bitwise_operator():
    print("\nBitwise Operators \n")
    a = 10
    b = 4

    print(a & b)
    print(a | b)
    print(~a)
    print(a ^ b)
    print(a >> 2)
    print(a << 2)


def arithmetic_operators():
    a = 15
    b = 4
    print("\nArithmetic Operators \n")
    # perform simple mathematical operations on values and variables (called as operands)
    print(f'Addition of {a} and {b} -> ', a + b)
    print(f'Subtraction of {a} and {b} -> ', a - b)
    print(f'Multiplication of {a} and {b} -> ', a * b)
    print(f'Division of {a} and {b} -> ', a / b)
    print(f'Modulus of {a} and {b} -> ', a % b)

    division_operator()

"""
    In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 
"""
def identity_operator():
    print("\nIdentity Operator \n")
    a = 10
    b = 20
    c = a

    print(a is not b)
    print(a is c)

"""
    In Python, in and not in are the membership operators that are used to test whether a value or variable is in a sequence.
"""
def membership_operator():
    print("\nMembership Operator \n")
    x = 24
    y = 20
    list = [10, 20, 30, 40, 50]

    if (x not in list):
        print("x is NOT present in given list")
    else:
        print("x is present in given list")

    if (y in list):
        print("y is present in given list")
    else:
        print("y is NOT present in given list")


"""
    in Python, Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. 

It simply allows testing a condition in a single line replacing the multiline if-else, making the code compact.
"""
def ternary_operator():
    print("\nTernary Operator \n")
    a, b = 10, 20
    min = a if a < b else b

    print(min)

if __name__ == '__main__':
    arithmetic_operators()
    comparison_operator()
    logical_operator()
    bitwise_operator()
    # Identity operator


