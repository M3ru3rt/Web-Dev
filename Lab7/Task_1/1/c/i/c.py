from math import sqrt

a, b = int(input()), int(input())

s = ""

for i in range(a, b+1):
    if int(sqrt(i))**2 == i:
        s = s + str(i) + " "

print(s)