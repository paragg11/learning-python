"""
Description - Arrange food according to calories. Reverse food items containing their calories.
3 methods:
- inbuilt method of python
- listname[::-1]
- swapping first element with last one and second element with second last one
"""

print("Enter the number of lists one by one.\n")

size = int(input("Enter the size of list : \n"))
mylist = []

for i in range(size):
    mylist.append(int(input("Enter the list element : ")))

print(f"Your list is {mylist}")

reverse1 = mylist
reverse1.reverse()

print(f"My first reversed list is {reverse1}")

reverse2 = mylist
print(f"My second reversed list is {reverse2[::-1]}")

reverse3 = mylist
for i in range(len(reverse1)//2):
    reverse3[i], reverse3[len(reverse1) - i - 1] = reverse3[len(reverse1) - i - 1], reverse3[i]

print(f"My third reversed list is {mylist}")