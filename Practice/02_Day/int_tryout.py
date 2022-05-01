import sys
print("NUMERIC CONTAINS INT, FLOAT AND COMPLEX NUMBER")

print("INTEGER")
num_int = 10    # int
print(num_int)
print("*" * 100)

num_negative_int = -1
print(f"The variable name is num_negavtive_int and the value is {num_negative_int} and type of it is {type(num_negative_int)}")

# TODO :- Please find this and edit this
num_mimimum_int = - sys.maxsize -1
num_maximum_int = sys.maxsize
num_maximum_int = sys.maxsize * 2 + 1
print(f"The variable name is num_mimimum_int and the value is {num_mimimum_int} and type of it is {type(num_mimimum_int)}")
print(f"The variable name is num_maximum_int and the value is {num_maximum_int} and type of it is {type(num_maximum_int)}")

num = num_maximum_int + 200
print(num)

# The below tryout is to understand the phenomena of dynamic type language.
# And python is dynamic type language
n :int = "10.0"
print(n)
n :str= "parag"
print(n)

digit = 1234567
print(len(digit))

"""
Traceback (most recent call last):
  File "D:\SparkEighteen\parag-intern\Practice\02_Day\int_tryout.py", line 39, in <module>
    int("ab")
ValueError: invalid literal for int() with base 10: 'ab'
"""
# the below statment will raise a ValueError
#int("ab")

"""
binary              01
hex                 06
octal               08
decimal             0 10

all the conversion

"""





number = int(input("Please type a number"))
if not isinstance(number,int):
    raise ValueError("It is not of type int")

