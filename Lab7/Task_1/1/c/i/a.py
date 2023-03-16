x = int(input())
y = int(input())

s = ""

for i in range(x, y + 1):
    if i % 2 == 0:
        s = s + str(i) + " "

print(s)