"""
Lecture 6 - Decisions
"""

if __name__ == "__main__":
    print("*" * 100)
    """
    Suppose we have a height measurements for two people, Chris and Sandy. 
    We have the tools to write a program that determines which height measurement is greater:
    """
    chris_height = float(input("Enter Chris's height (in cm): "))
    sandy_height = float(input("Enter Sandy's height (in cm): "))
    print("The greater height is", max(chris_height, sandy_height))

    print("*" * 100)
    """
    But, we don’t have the tools yet to decide who has the greater height. For this we need if statements:
    """
    chris_height = float(input("Enter Chris's height (in cm): "))
    sandy_height = float(input("Enter Sandy's height (in cm): "))
    if chris_height > sandy_height:
        print("Chris is taller")
    else:
        print("Sandy is taller")

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

    print("*" * 100)
    name1 = "Dale"
    print("Enter the height of", name1, "in cm ==> ", end='')
    height1 = int(input())

    name2 = "Erin"
    print("Enter the height of", name2, "in cm ==> ", end='')
    height2 = int(input())

    if height1 < height2:
        print(name2, "is taller")
        max_height = height2

    if height1 >= height2:
        print(name1, "is taller")
        max_height = height1

    print("The max height is", max_height)

    print("*" * 100)
    name1 = "Dale"
    height1 = int(input("Enter the height of " + name1 + " in cm ==> "))

    name2 = "Erin"
    height2 = int(input("Enter the height of " + name2 + " in cm ==> "))

    if height1 < height2:
        print(name2, "is taller")
        max_height = height2
    else:
        print(name1, "is taller")
        max_height = height1

    print("The max height is", max_height)

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

