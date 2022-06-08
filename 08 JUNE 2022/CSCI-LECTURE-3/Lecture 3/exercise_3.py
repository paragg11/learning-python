if __name__ == "__main__":
    print()

    #More than just numbers

    print('Hello World')
    x = 8
    y = 10
    print('Value of x is', x, 'Value of y is', y)

    print("*" * 100)
    """
    String defination
    """
    print('Rensselaer')
    print("Albany, NY")
    print('4 8 15 16 23 42')
    s = 'Hello'
    t = 'Good-bye'
    print(s)
    print(t)

    print("*" * 100)
    """
    Combining single and double quotes in strings
    """
    s = 'He said, "Hello, World!"'
    print(s)
    t = "Many many quotes here ''''''' and here ''' but correct"
    print(t)

    print("x" * 100)
    """
    Multi-Line Srings
    """
    s1 = """ This
    is a multi-line
    string.
    """
    print(s1)
    s1
    'This\nis a multi line\nsting.'
    print(s1)

    print('*' * 100)
    """
    Escape characters
    """
    s0 = "*\t\n**\t**\n***\t***\n"
    print(s0)
    s1 = "I said,\"This is a valid string.\""
    print(s1)

    print('*' * 100)
    """
    String Operations - Concatenation
    """
    s0 = "Hello"
    s1 = "World"
    print(s0 + s1)
    print(s0+ ' ' +s1)
    s0 = "hello"
    s1 = "world"
    print(s0, s1)

    print("*" * 100)
    '''
    String Operations — Replication
    '''
    s = 'HA'
    print('s' * 10)
    # print('Hello' * 8.1)    #TypeError: can't multiply sequence by non-int of type 'float'
    # print('123' + 4)        #TypeError: can only concatenate str (not "int") to str

    print('*' * 100)
    """
    
    """
    s1 = '"Hi mom", I said.  "How are you?"'
    print(s1)                                       # Valid string
    s2 = '"Hi mom", I said.  '"How are you?"
    print(s2)                                       #Invalid string
    # s3 = '"Hi mom", I said.  '"How are you?"'       #Invalid string (syntax error)
    # print(s3)
    s4 = """'Hi mom", I said.  '"How are you?"'"""      #Valid string
    print(s4)
    # s5 = ""I want to be a lion tamer!"'         #Invalid string (syntax error)
    s6 = "\"Is this a cheese shop?\"\n\t'Yes'\n\t\"We have all kinds!\""
    print(s6)           #Invalid string    -> Valid string

    print('*' * 100)
    """
    What is the output?
    """
    s = "Cats\tare\n\tgood\tsources\n\t\tof\tinternet\tmemes"
    """
    Cats    are
        good    sources
            of  internet    memes
    """
    print(s)

    print("*" * 100)
    """
    What is the output?
    """
    print('\\' * 4)    #\\\\
    print('\\\n' * 3)
    print('Good-bye')

    # print("*" * 100)
    """
    Which of the following are legal? For those that are, 
    show what Python outputs when these are typed directly into the interpreter.
    """
    # 'abc' 'def'
    # 'abc' + 'def'
    # 'abc ' + 'def'
    # x = 'abc'
    # y = 'def'
    # x + y
    # x
    # y
    # s1 = 'abc' * 4
    # s1
    # s2 = 'abc ' * 4
    # print(s2)

    print('*' * 100)
    """
    String Operations — Functions
    """
    s = "Hello!"
    print(len(s))   #6

    print('*' * 100)
    """
    User Input
    """
    # print("Enter a number:")                                          10
    # x = float(input())                                                10.0
    # print('The square of', x, 'is', x*x)

    # x = input("Enter a number:")                                      10
    # x = float(x)                                                      10.0
    # print('The square of', x, 'is', x * x)

    # x = input("Enter an integer:")
    # x = int(x)
    # print(x)

    print('*' * 100)
    """
    Practice Problems 
    What is the output for this Python program?
    """
    print(len('George'))                        #6
    print(len(' Tom   '))                       #7
    s = """Hi
    sis!
    """
    print(len(s))                               #6(In unix its \n) -> 16(In Linus its \r\n \r -> beginning of line)

    print('*' * 100)
    """
    Which of the following are legal? For those that are, 
    show what Python outputs when these are typed directly into the interpreter.
    """
    # 'abc' + str(5)                      #'abc5'
    # 'abc' * str(5)                      #TypeError: can't multiply sequence by non-int of type 'str'
    # 'abc' + 5                           #TypeError: can only concatenate str (not "int") to str
    # 'abc' * 5                           #'abcabcabcabcabc'
    # 'abc' + 5.0                         #TypeError: can only concatenate str (not "float") to str
    # 'abc' + float(5.0)                  #TypeError: can only concatenate str (not "float") to str
    # str(3.0) * 3                        #'3.03.03.0'

    print('*' * 100)
    """
    What is the output of the following when the user types 4 when running the following Python program?
    """
    # x = input('Enter an integer ==> ')
    # x = x * 2
    # x = int(x)
    # x *= 2
    # print('x is:', x)

    print('*' * 100)
    """
    What is the output when the user types the value 64 when running the following Python program?
    """
    # x = input('Enter an integer ==> ')
    # y = x // 10
    # z = y % 10
    # print(x, ',', y, z, sep='')
    #TypeError: unsupported operand type(s) for //: 'str' and 'int'

    # SOLUTION
    x = int(input('Enter an integer ==> '))
    y = x // 10
    z = y % 10
    print(x, ',', y,',', z, sep='')

    print("*" * 100)
    """
    Write a program that requests an integer from the user as an input and stores in the variable n. 
    The program should then print n 1’s with 0’s inbetween. 
    For example if the user input the value 4 then the output should be
    """
    n = int(input('Enter an integer: '))

    




