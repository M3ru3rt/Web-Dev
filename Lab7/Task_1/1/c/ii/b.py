n = int(input())

i = 2

while n >= 2:
    if n % i == 0:
        print(i)
        break
    i = i + 1