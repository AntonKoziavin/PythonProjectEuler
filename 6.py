number1 = 0
number2 = 0
for i in range(1, 101):
    number1 += i**2                             # Сумма квадратов
    number2 += i                                # Сумма всех i для дальнейшего возведения в квадрат
print(number2**2 - number1)

