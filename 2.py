a = 1
fib = 0
b = 0
c = 0
while c in range(4000000):
    c = a + b
    a += b
    b = a - b
    if c < 4000000:
        zero = c % 2
        if zero == 0:
            fib += c
print(fib)
