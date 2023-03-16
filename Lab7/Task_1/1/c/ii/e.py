n = int(input())

k = 0

p = 1

while n > p:
    p <<= 1
    k += 1
print(k)