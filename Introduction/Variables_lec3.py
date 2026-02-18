
"""
    Variable - A variable is a named memory location to store data that can be referenced and manipulated during the program execution
    It is essentially a name assigned to a value

    Python variables do not require explicit declaration like in Java and other compiled languages
    The type of the variable is assigned using the value assigned to it

    Naming Convention
        can only contain letters, digits and _ ( cannot start with a digit), case-sensitive, no reserved keywords allowed

    Python variables are dynamic typed - same variable can hold different types during program execution

    Type casting using int(), float(), str() function
    Check type of any variable using the type(<variable>) function

"""


def learn_variables():
    name = "Variable1"
    age = 22

    # Name is of type str and age is int type assigned based on the right side value
    print(name, age, type(name), type(age))

    ## Dynamic type
    name = "alex"
    name = 22

    ## Multiple assignments
    x , y, z = 20, 30, "python"
    print(x, y, z)

    x = y = z = 100

    #Typecast a variable
    age = "22"
    print("Convert to int", int(age))
    print("Convert to float", float(age))
    name = 25
    print("Convert to str", str(name))

    # Variable types
    a = 25
    b = "string"
    c = 5.0
    d = [1,2,4,5]
    e = {'key':'value'}
    f = True

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))


if __name__ == '__main__':
    learn_variables()