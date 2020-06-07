z = 0
x = 0
c = 0
for a in range(1,1000):
    i = a % 3
    if i == 0:
        z += a
print(z)
for a in range(1,1000):
    i = a % 5
    if i == 0:
        x += a
print(x)
for a in range(1,1000):
    i = a % 15
    if i == 0:
        c += a
print(c)
print(z+x-c)
