n = input()

a = 0

for i in range(0, len(n)):
    a = a + int(n[i])*(2**(len(n)-i-1))
print(a)