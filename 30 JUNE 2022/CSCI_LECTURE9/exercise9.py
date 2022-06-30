if __name__ == "__main__":

    """
    Lecture 9 — While Loops
    """

    print("*" * 100)
    """
    Basics of while
    """
    i = 1
    while i < 10:
        print(i)
        i += 1

    print("*" * 100)
    """
    Using Loops with Lists
    """
    co2_levels = [(2001, 320.03), (2003, 322.16), (2004, 328.07), \
                  (2006, 323.91), (2008, 341.47), (2009, 348.92), \
                  (2010, 357.29), (2011, 363.77), (2012, 361.51), \
                  (2013, 382.47)]

    i = 0
    while i < len(co2_levels):
        print("Year", co2_levels[i][0], \
              "CO2 levels:", co2_levels[i][1])
        i += 1

    print("*" * 100)
    """
    
    """

