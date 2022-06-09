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
    name = name.replace('a',total_new)
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