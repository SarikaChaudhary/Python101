"""
    Data Types tell us about the type of data values
    It defines the type of value a variable can hold, the range of possible values, the operations that can be performed, and how it is stored in memory.
    Everything is an object in python programming language so data types are the classes
    and the variables (objects) are the instances of these classes.

    1.  Numeric: int, float, complex
    2. Sequence Type: string, list, tuple
    3.Mapping Type: dict
    4. Boolean: bool
    5. Set Type: set, frozenset
    6. Binary Types: bytes, bytearray, memoryview

"""

"""
    In python 2.x, an implicit str type is ASCII
    In python 3.x, an implicit str type is Unicode
"""


def string_datatype():
    print("\n String Data Types\n")
    # Python Strings are array of bytes representing Unicode characters

    s = "This is a string"
    print(s)

    print(type(s))  ##  str
    print(type(b'byteString'))  ## bytes
    print(type(u'unicodeStr'))  ## str

    # You can access the string elements using indexes
    print(s[0])
    print(s[1])
    print(s[-1])  ## last char


"""
    Lists are similar to arrays found in other languages. They are an ordered and mutable collection of items. 
    It is very flexible as items in a list do not need to be of the same type. 
"""


def list_datatype():
    print("\n List Data Type\n")
    a = []
    b = [1, 2, 3, "Heels", "asda"]
    print(b[-1])  # asda


"""
    Tuple is an ordered collection of Python objects. The only difference between a tuple and a list is that tuples are immutable. 
    Tuples cannot be modified after it is created.
"""


def tuple_datatype():
    print("\n Tuple Data Type\n")
    tup1 = ()
    tup2 = ("ele1",)
    tup3 = ("ele1", "ele2")
    print(tup1, tup2, tup3)
    print(tup1[0], tup2[1], tup3[-1])


"""
    In Python Data Types, Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. 
    The order of elements in a set is undefined though it may consist of various elements. 
"""
def set_datatype():
    print("\n Set Data Type\n")
    set1 = set()
    set2 = set("GeeksForGeeks")
    set3 = {"a", "b", "c", "a"}  ## set(["a","b","c"])

    ## Set Items cannot be referenced using an index since the sets are unordered the items have no index.
    print(set3)

    # loop through the set
    for item in set3:
        print(item,end=" ")

    # check if an element is in set
    print("a" in set3)

"""
    A dictionary in Python is a collection of data values, used to store data values like a map, unlike other Python Data Types, a Dictionary holds a key: value pair. Key-value is provided in dictionary to make it more optimized. 
    Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’. 
    Values in a dictionary can be of any datatype and can be duplicated, whereas keys can’t be repeated and must be immutable.

    Note:
    Starting from Python 3.7, dictionaries (dict) also maintain the insertion order of keys by default.
"""
def dict_datatype():
    print("\n Dictionary Data Type\n")
    dict1 = {}
    dict1["key1"] = "value1"
    dict1["key2"] = "value2"
    print(dict1)

    dict2 = {1: "valu1", 'name': "value2", 3: "value3"}
    print(dict2)

    dict3 = dict({1: "value1", 'name': "value2", 3: "value3"})
    print(dict3)
    print(dict3["name"])
    print(dict3.get(3)) # using key


    # Print a dictionary
    d = dict({'x': 123, 'y': 354})
    for x in d:
        print("%s  %d" % (x, d[x]))


""" Sequence Data Types -
    A sequence is an ordered collection of items, which can be of similar or different data types. 
    Sequences allow storing of multiple values in an organized and efficient fashion
"""


def sequence_datatype():
    print("\nSequenced datatype\n")
    string_datatype()
    list_datatype()
    tuple_datatype()


def datatypes():
    print("\nNumeric Data types\n")
    a = 5
    b = 3.0
    inf_var =  float('inf')  ## float('inf') creates a floating-point number representing positive infinity.
    c = 1 + 3j
    print(f' type of {a} = {type(a)}')
    print(f' type of {b} = {type(b)}')
    print(f' type of {c} = {type(c)}')

    sequence_datatype()

    ## Bool data type
    ## True / False

    ## 1 - Truthy value (Evaluates to True in conditional context like a if condition)
    ## 0 - Falsy value (evaluates to False)
    if 1:
        print(" 1 is truthy")
    if not 0:
        print(" 0 is falsy")

    ##


if __name__ == '__main__':
    datatypes()
