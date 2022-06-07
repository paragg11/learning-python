"""
j = 2
Loop from 1 to 11
    result = j * i
    Print(result)

"""
j = 2
for i in range(1,11):
    result = j * i
    print(f"{j} * {i} = {result}")

"""
loop 2 to 13
    Loop from 1 to 11
        result = j * i
        Print(result)

"""
for j in range(2,13):
    for i in range(1,11):
        result = j * i
        print(f"{j} * {i} = {result}")

"""

loop 1 to 13
    Loop from 1 to 11
        result = j * i
        Print(result, end = "\t")
    print()
"""

for j in range(1,13):
    for i in range(1,11):
        result = j * i
        print(result, end = "\t")
    print()