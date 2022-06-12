if __name__ == "__main__":
    
    print('*' * 100)
    """
    Objects & Methods
    """

    b = 'good morning'
    print(b.count('o'))

    print('*' * 100)
    """
    String Methods
    """
    name = "Neil Degrasse Tyson"
    print(name.lower())
    lowername = name.lower()
    print(lowername.upper())
    print(lowername.capitalize())
    print(lowername.title())
    print('abracadabra'.replace('br','dr'))
    print('abracadabra'.replace('a',''))
    print('Neil Degrasse Tyson'.find(" "))
    print('Neil Degrasse Tyson'.find("a"))
    print('Neil Degrasse Tyson'.find("x"))
    print("Monty Python".count('o'))
    print("aaabbbfsassassaaaa".strip("a"))
    episode = "Chesse Shop"
    print(episode.lower())
    print(len(episode))
    print(episode + "!")

    print('*' * 100)
    """
    Practice Problems 1
    1. Write code that takes a string in a variable called phrase and prints the string with all vowels removed.
    """

    phrase = 'iiisahckjasbchjgsacnkasjchbslcnse'
    print(phrase)
    phrase = phrase.replace('a','')
    phrase = phrase.replace('e','')
    phrase = phrase.replace('i','')
    phrase = phrase.replace('o','')
    phrase = phrase.replace('u','')
    print(phrase)

    print('*' * 100)
    """
    2. Create a string in a variable and assign it to a variable called name. 
    Write code to create a new string that repeats each letter a in name as many times as a appears in name 
    (assume the word is all lower case).
    """
    name = 'amos eaton'
    total_count = name.count('a')
    total_new = 'a' * total_count
    name = name.replace('a', total_new)
    print(name)

    print('*' * 100)
    """
    3. Given a string in a variable called name, switch all letters a and e (only lowercase versions). 
    Assume the variable contains only letters and spaces.
    Hint: first replace each ‘a’ with ‘1’.
    """
    name = 'Rensselaer Polytechnic Institute'
    name = name.replace('a', '1')
    name = name.replace('e', 'a')
    name = name.replace('1', 'e')
    print(name)

    print("*" * 100)
    """
    String Format Method
    """
    pi = 3.14159
    r = 2.5
    h = 10 ** 0.5
    volume = pi * r ** 2 * h
    print('A cylinder of radius', r, 'and height', h, 'has volume', volume)

    print('*' * 100)
    out_string = 'A cylinder of radius {0:.2f} and height {1:.2f} has volume {2:.2f}'.format(r, h, volume)
    print(out_string)

    print("*" * 100)
    """
    Modules
    """
    import math
    print(math.sqrt(49))
    print(math.trunc(5))
    print(math.ceil(4.5))
    print(math.log(1024,2))
    print(math.pi)

    from math import sqrt, pi
    import math as m
    print(m.pi)
    print(m.sqrt(16))

    print('*' * 100)
    """
    The math module contains the constant e as well as pi. 
    Write code that prints these values accurate to 3 decimal places and then write code that computes and outputs
    πe and eπ
    both accurate to 2 decimal places.
    """
    m.pi
    f = '{:.3f}'.format(m.pi)
    print(f)
    print(m.pi**m.e)
    new_value = m.pi**m.e
    f = '{:.2f}'.format(new_value)
    print(f)
    second_value = m.e**m.pi
    f = '{:.2f}'.format(second_value)
    #f =f'{second_value.{:.2f}}'
    print(f)

    print('*'*100)
    """
    Write a short program to ask the user to input height values (in cm) three times. 
    After reading these values (as integers), 
    the program should output the largest, the smallest and the average of the height values.
    """

    # first_value = int(input())
    # second_value = int(input())
    # third_value = int(input())
    # new = [first_value, second_value, third_value]
    # print(new)
    # print(min(new))
    # print(max(new))
    # print(sum(new)//len(new))
    #
    # print('*' * 100)
    """
    What happens when we type
    and then use math.pi?
    """
    #math.pi = 3
    print(math.pi)

    print("*" * 100)
    """
    Write a program that assigns a string to the variable called phrase and 
    then transforms phrase into a hashtag. 
    In other words, all words in phrase are capitalized, all spaces are removed, and a # appears in front. 
    Store the result in a variable called hashtag. 
    Then print the value of both phrase and hashtag. Your program should start with
    phrase = 'Things you wish you knew as a freshman'
    and the output from the program (using print() function calls) should be
    The phrase "Things you wish you knew as a freshman"
    becomes the hashtag "#ThingsYouWishYouKnewAsAFreshman"
    Note that the output includes the quotation marks.
    """

    phrase = 'Things you wish you knew as a freshman'
    phrase = phrase.capitalize()
    print(phrase)
    phrase = phrase.replace(' ', '')
    print(phrase)
    #phrase = ''.join(phrase)
    print('#'+ phrase)

    print("*" * 100)
    """
    One of the challenges of programming is that there are often many ways to solve even the simplest problem. 
    Consider computing the area of the circle with the standard formula
    a(r)=πr2
    Fortunately, we now have pi from the math module, but to compute the square of the radius we now can use ** or pow() or
    we can just multiply the radius times itself. To print the area accurate to only a few decimal places we can now use the string format() method or the round() built-in function, 
    which includes an optional second argument to specify the number of decimal places.
    Write a short Python program that computes and prints the areas of two circles, 
    one with radius 5 and the other with radius 32. 
    Your code must use ** once and pow() once and it must use format() once and round() once. 
    The output should be exactly
    Area 1 = 78.54
    Area 2 = 3216.99
    """

    radius = 5
    area = m.pi * radius**2
    f = '{:.2f}'.format(area)
    print(f)

    radius2 = 32
    area2 = m.pi * pow(32, 2)
    print(area2)
    print(round(3216.990877275948, 2))
