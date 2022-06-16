"""
Lecture 6 - Decisions
"""

if __name__ == "__main__":
    print("*" * 100)
    """
    Suppose we have a height measurements for two people, Chris and Sandy. 
    We have the tools to write a program that determines which height measurement is greater:
    """
    # chris_height = float(input("Enter Chris's height (in cm): "))
    # sandy_height = float(input("Enter Sandy's height (in cm): "))
    # print("The greater height is", max(chris_height, sandy_height))

    print("*" * 100)
    """
    But, we don’t have the tools yet to decide who has the greater height. For this we need if statements:
    """
    # chris_height = float(input("Enter Chris's height (in cm): "))
    # sandy_height = float(input("Enter Sandy's height (in cm): "))
    # if chris_height > sandy_height:
    #     print("Chris is taller")
    # else:
    #     print("Sandy is taller")

    print("*" * 100)
    """
    Boolean Values
    """
    x = True

    print("*" * 100)
    """
    Relational Operators - Less than and greater than
    """
    # x = 17
    # y = 15.1
    # x < y  #False
    # var = x <= y  #False
    # x <= 17    #True
    # y < x  #True

    # s1 = 'art'
    # s2 = 'Art'
    # s3 = 'Music'
    # s4 = 'music'
    # s1 < s2     #False
    # s2 < s3     #True
    # s2 < s4     #True
    # s1 < s3     #False

    # print("*" * 100)
    # name1 = "Dale"
    # print("Enter the height of", name1, "in cm ==> ", end='')
    # height1 = int(input())
    #
    # name2 = "Erin"
    # print("Enter the height of", name2, "in cm ==> ", end='')
    # height2 = int(input())
    #
    # if height1 < height2:
    #     print(name2, "is taller")
    #     max_height = height2
    #
    # if height1 >= height2:
    #     print(name1, "is taller")
    #     max_height = height1
    #
    # print("The max height is", max_height)

    # print("*" * 100)
    # name1 = "Dale"
    # height1 = int(input("Enter the height of " + name1 + " in cm ==> "))
    #
    # name2 = "Erin"
    # height2 = int(input("Enter the height of " + name2 + " in cm ==> "))
    #
    # if height1 < height2:
    #     print(name2, "is taller")
    #     max_height = height2
    # else:
    #     print(name1, "is taller")
    #     max_height = height1
    #
    # print("The max height is", max_height)

    print("*" * 100)
    """
    More complex boolean expression, starting with and
    """
    cel_today = 12
    cel_yesterday = -1
    if cel_today > 0 and cel_yesterday > 0:
        print("It was above freezing both yesterday and today.")

    print("*" * 100)
    """
    More complex boolean expressions - or
    """
    cel_today = 12
    cel_yesterday = -1
    if cel_today > 0 or cel_yesterday > 0:
        print("It has been above freezing in the last two days.")
    """
    The boolean expression is True if ANY of the following occurs

    the left relational expression is True,
    the right relational expression is True,
    both the left and right relational expression are True.
    """

    print("*" * 100)
    """
    Boolean Logic - not
    """
    a = 15
    b = 20
    if not a < b:
        print("a is not less than b")
    else:
        print("a is less than b")

    print("*" * 100)
    """
    Does a given point fall within a rectangle
    Program to demonstrate the use of complex boolean expressions and if/elif/else
    clauses. Determine whether a set of coordinates fall within a rectangle given
    by the verticies (x0, y0), (x0, y1), (x1, y1), and (x1, y0)
    Initialize the rectangle
    """
    x0 = 10
    x1 = 16
    y0 = 32
    y1 = 45

    # x = input("x co-ordinate is :")
    # print(x)
    # x = float(x)
    # y = input("y co-ordinate is :")
    # print(y)
    # y = float(y)
    #
    # if (x0 == x or x == x1) and (y0 <= y <= y1) or (y0 == y or y == y1) and (x0 <= x <= x1):
    #     print("Point ({:.2f},{:.2f}) is on the boundary.".format(x, y))
    #
    # elif (x0 < x < x1) and (y0 < y < y1):
    #     '''
    #     If we are not on the boundary, but we are in range in both x and y,
    #     then we are inside the rectangle
    #     '''
    #     print("Point ({:.2f},{:.2f}) is inside the rectangle.".format(x, y))
    # else:
    #     '''
    #     If we are not on the boundary and we are not inside the rectangle, then
    #     we must be outside.
    #     '''
    #     print("Point ({:.2f},{:.2f}) is outside the rectangle.".format(x, y))

    print("*" * 100)
    """
    Consider the following boolean expressions:
    """
    # a < b   #False
    # a < abs(b)      #True
    # a >= c          #False
    # s < t           #False
    # t == v          #False
    # u == w     #False
    # b < y       #true

    print("*" * 100)
    """
    Consider the following boolean expressions:
    """
    # x =15
    # y = -15
    # z = 32
    # x == y and y < z    #FALSE
    # x == y or y < z     #TRUE
    # x == abs(y) and y < z   #TRUE
    # x == abs(y) or y < z    #TRUE
    # not x == abs(y)     #FALSE
    # not x != abs(y)     #TRUE


    # TRUE AND TRUE -> True
    # TRUE AND FALSE -> False
    # FALSE AND TRUE -> False
    # FALSE AND FALSE -> False

    # TRUE OR TRUE -> True
    # TRUE OR FALSE -> True
    # FLASE OR TRUE -> True
    # FALSE OR FALSE -> False

    print("*" * 100)
    """
    So far we have assumed all input to our programs is correct. In practice, 
    however, programs must do extensive error checking. 
    Here is a slightly-contrived problem to illustrate this: 
    Write a short program that asks the user to input two numbers where one of them must be greater than 10 
    and the other must be less than or equal to 10. 
    It does not matter which is which. 
    If both inputs are greater than 10, 
    the program should output the error message “Both are above 10.” 
    If both are less than or equal 10, 
    the program should output the message “Both are below 10.” 
    If the one of the numbers is above 10 and the other is less than or equal to 10, 
    no message should be output. 
    Regardless of any messages, 
    the program should then output the average of the two numbers, 
    accurate to 2 decimals. 
    This program must use one if, one elif and no else. 
    Note: just like in HW 1, 
    the program should output a value immediately after reading it. 
    Also, if you are having problems matching our output format, 
    explore the difference between the output of the following two lines
    """
    n = int(input("Enter the first number: "))
    print(n)
    m = int(input("Enter the second number: "))
    print(m)

    if (n >= 11) or (m >= 11):
        print("Both are above 10.")
    elif n < 10 or m < 10:
        print("Both are below 10.")

    avg = (n + m)/2
    print("Average of two nos is ", avg)            #TODO - how to write without else
