"""
INPUT - TAKE INPUT X, MAX NOS AND MIN NOS

OUTPUT - PRINT WHETHER THE NOS BETWEEN MAX AND MIN NOS IS DIVISBLE BY INPUT OR NOT
"""


apples = int(input("Enter the total no. of apples:\n"))
min_apples = int(input("Enter the minimum no. of apples:\n"))
max_apples = int(input("Enter the maximum no. of apples:\n"))

for i in range(min_apples,max_apples+1):
    if apples % i == 0:
        print(f"{i} is divisible by {apples}")
    else:
        print(f"{i} is not divisible by {apples}")