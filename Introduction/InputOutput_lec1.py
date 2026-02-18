
def input_output():
    # Input
    # Take 1 String as Input - your name
    name = input("Hey, tell me your name ?")
    print(f'Thank you for your name, {name}!')

    # Take a number as input
    # This requires typecasting as default input type is string

    """ ExceptionHandling -> ValueError if input is non-numeric string
        input() function returns the input as a string. When int() tries to convert the string '1.5' into an integer, 
        it raises a ValueError because '1.5' is not a valid integer literal.
    """
    age = int(input("what is your age?"))
    print(f'You are {age} years old')

    ## Take multiple numbers/strings as input
    x, y = input("tell me about x and y?").split()
    print(x, y)

    ## Know about the type of any variable
    print(type(name))
    print(type(age))
    print(type(x), type(y))

    # In Python, if you multiply a string by a number, it just repeats the string that many times.
    a = "5"
    b = "2"
    print(a * 3) # "555"

    # x and y are strings, so the '+' operator concatenates them.
    print(a + b) # output is 52

if __name__ == '__main__':
    input_output()