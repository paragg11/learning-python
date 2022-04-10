def print_rangoli1(n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(n)]
    print(data)
    items = list(range(n))
    print(items)
    items = items[:-1]+items[::-1]
    for i in items:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))

import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    n = size
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))

#print_rangoli(10)

print("Abrar")
print_rangoli1(10)