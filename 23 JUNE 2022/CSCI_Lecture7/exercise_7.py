"""
Lecture 7 - Lists part 1
"""

if __name__ == "__main__":
    print("*" * 100)
    scores = [59, 61, 63, 63, 68, 64, 58]
    print(scores)
    planets = ['Mercury', 'Venus', 'Earth', 'Mras', 'Jupiter',
               'Saturn', 'Neptune', 'Uranus', 'Pluto']
    print(planets)
    planets[3] = 'Mars'
    print(planets)
    print(scores[4])

    print("*" * 100)
    s = 'abc'
    print(s[0])
    print(s[1])

    print("*" * 100)
    print("Average Scores = {:.2f}".format(sum(scores) / len(scores)))
    print("Max Score =", max(scores))
    print("Min Score =", min(scores))

    print("*" * 100)
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune', 'Uranus', 'Pluto']
    planets = planets.sort()
    print(planets)

    print("*" * 100)
    """
        So, the function returns nothing! But, it does change the value of the input list.
        This is the first such function we have seen.
        It does so because lists are containers, and functions can manipulate what is inside containers.
        Functions cannot do so for simple types like integer and float.
    """
    scores = [59, 61, 63, 63, 68, 64, 58]
    new_scores = scores.sort()
    print(scores)
    print(new_scores)


    print("*" * 100)
    """
    If we want a new list that is sorted without changing the original list then we use the sorted() function:
    """
    scores1 = [59, 61, 63, 63, 68, 64, 58]
    new_scores = sorted(scores1)
    print(scores1)
    print(new_scores)

    print("*" * 100)
    l = ['Alice', 3.75, ['math', 'csci', 'psyc'], 'PA']
    print(l[0])
    print(l[1])
    print(l[2])
    print(l[2][0])
    print(l[3])

    print("*" * 100)
    """
    Write three different ways of removing the last value — 'Pluto' — from the list of planets. 
    Two of these will use the method pop.
    """
    planets = ['Mercury', 'Venus', 'Earth', 'Mras', 'Jupiter',
               'Saturn', 'Neptune', 'Uranus', 'Pluto']
    planets.pop(-1)
    print(planets)
    planets = ['Mercury', 'Venus', 'Earth', 'Mras', 'Jupiter',
               'Saturn', 'Neptune', 'Uranus', 'Pluto']
    planets.pop(8)
    print(planets)
    planets = ['Mercury', 'Venus', 'Earth', 'Mras', 'Jupiter',
               'Saturn', 'Neptune', 'Uranus', 'Pluto']
    planets.remove('Pluto')
    print(planets)

    print("*" * 100)
    """
    Write code to insert 'Asteroid belt' between 'Mars' and 'Jupiter'.
    """
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter',
               'Saturn', 'Neptune', 'Uranus', 'Pluto']
    planets.insert(4, 'Asteroid belt')
    print(planets)

    print("*" * 100)
    """
    Can you name a list a number in Python?
    Python has some conventions for variable names. 
    You can use any letter, the special characters “_” and every number provided you do not start with it. 
    White spaces and signs with special meanings in Python, as “+” and “-” are not allowed.
    """
    # l1 = [6, 12, 13, 'hello']
    # print(l1[1], l1[-2])        #12 13
    # l1.append(15)               #
    # print(len(l1))              #5
    # print(len(l1[3]))           #5
    # l1.pop(3)                   #'hello'
    # l1.sort()                   # [6, 12, 13, 15]
    # l1.insert(2, [14, 15])      # [6, 12, [14, 15], 13, 15]
    # l1[3] += l1[4]              #28
    # l1[3] += l1[2][1]           #43
    # print(l1[3])                #43
    # l1.pop()                    #15
    # l1[2].remove(14)            #14
    # print(l1)                   #[6, 12, [15], 43]

    print("*" * 100)
    """
    Write a short Python program that starts with the list
    values = [ 14, 10, 8, 19, 7, 13 ]
    (The above statement list should be the first line of your program.) Then add code that does the following steps:

    1. Reads an integer, prints it (as we have done for input when using Submitty), 
       and appends it to the end of values.
    """
    values = [14, 10, 8, 19, 7, 13]
    values.append(15)
    print(values[-1])

    """
    2. Reads another integer, prints it and inserts it at index location 2 of values.
    """
    print(values)
    values.insert(2, 23)
    print(values)

    """
    3. Prints the integer at index 3 of values and print the integer at index -1 of values, both on one line.
    """
    print(values[3], values[-1])

    """
    4. Prints the difference between the maximum and minimum of the integers in values. 
    """
    print(max(values))
    print(min(values))
    print("Difference is ", max(values)-min(values))

    """
    5. Prints the average of the integers in values, accurate to one decimal place. 
       This must use the functions sum() and len()
    """

    average = sum(values)/len(values)
    print(average)
    print("Average is ({:.1f})".format(average))

    """
    7. Prints the median of the numbers in values.  
       Since the list is even length (a fact that you are allowed to use, just for this exercise), 
       this is the average of the two middle integers after values is sorted.
    """

    print(values)
    values.sort()
    print(values)
    print("Median is : ", ((values[3]+values[4])/2))