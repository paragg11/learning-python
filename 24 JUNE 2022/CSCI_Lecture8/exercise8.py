"""
Lecture 8 — Tuples, Modules, Images
"""
if __name__ == "__main__":


    x = (4, 5, 10)
    print(x[0])
    print(x[2])
    print(len(x))

    s = 'abc'
    print(s[0])
    print(s[1])

    # x[1] = 2
    # TypeError: 'tuple' object does not support item assignment

    # s[1] = 'A'
    # TypeError: 'tuple' object does not support item assignment

    print("*" * 100)
    """
    What are tuples good for?
    """

    # 2, 3
    # (2, 3)
    # x = 2, 3
    # a, b =x
    # a
    # 2
    # b
    # 3
    # c, d = 3, 4
    # c
    # 3
    # d
    # 4

    print("*" * 100)
    def split(n):
        """Split a two-digit number into its tens and ones digit """
        tens = n // 10
        ones = n % 10
        return (tens, ones)

    x = 83
    ten, one = split(x)
    print(x, "has ten digits", ten, "and one digit", one)

    print("*" * 100)
    def combine(digits):
        return digits[0]*100 + digits[1]*10 + digits[2]

    d = (5, 2, 7)
    print(combine(d))

    print("*" * 100)
    """
    Area and Volume Module
    """
    import lec08_area

    r = 6
    h = 10
    a1 = lec08_area.circle(r)
    a2 = lec08_area.cylinder(r, h)
    a3 = lec08_area.sphere(r)
    print("Area circle {:.1f}".format(a1))
    print("Surface area cyclinder {:.1f}".format(a2))
    print("Surface area sphere {:.1f}".format(a3))

    print("*" * 100)
    def f1(x,y):
        return x+y

    def f2(x):
        return x+y

    x = 5
    y = 10

    print('A:', f1(x,y))     #15
    print('B:', f1(y,x))     #15
    print('C:', f2(x))       #15
    print('D:', f2(y))       #20    TODO - how 20 didnt get this
    #print('E:', f1(x))       #TypeError: f1() missing 1 required positional argument: 'y'

    print("*" * 100)
    """
    What is the exact output of the following Python code? 
    What are the global variables, the function arguments, the local variables, and the parameters in the code?
    """
    x = 3
    def do_something(x, y):
        z = x + y
        print(z)
        z += z
        print(z)
        z += z * z
        print(z)


    do_something(1, 1)
    y = 1
    do_something(y, x)

    print("*" * 100)
    """
    Write a Python function that takes two strings as input and 
    prints them together on one 35-character line, with the first string left-justified, 
    the second string right-justified, and as many periods between the words as needed. For example, the function calls
    """
    def print_left_right(l, r):
        x = 35 - len(l) - len(r)
        z = l + '.' * x + r
        print(z)

    print_left_right('apple', 'banana')
    print_left_right('syntax error', 'semantic error')

    print("*" * 100)
    """
    Write a program that reads Erin’s height (in cm), Erin’s age (years), Dale’s height (in cm) and Dale’s age (years) 
    and tells the name of the person who is both older and taller or tells that neither is both older and taller.
    """
    eh = int(input("Erin's height => "))
    ea = int(input("Erin's age =>"))
    dh = int(input("Dale's height => "))
    da = int(input("Dale's age => "))

    ## check erin first
    if eh > dh and ea > da:
        print("Erin is older and taller")
    elif dh > eh and da > ea:
        print("Dale is older and taller")
    else:
        print("No one is older and taller")

    print("*" * 100)
    """
    In the United States, a car’s fuel efficiency is measured in miles driven per gallon used. 
    In the metric system it is liters used per 100 kilometers driven. 
    Using the values 1.609 kilometers equals 1 mile and 1 gallon equals 3.785 liters,
    write a Python function that converts a fuel efficiency measure in miles per gallon to one in liters per 100 kilometers 
    and returns the result.
    """

    