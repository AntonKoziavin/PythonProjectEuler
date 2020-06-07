import math


string = 20
strings = [0] * string
tab = [strings] * string
for item in tab:
    print(item, end="\n")
print("Использование биноминального коэффициента")
print(int(math.factorial(string*2)/(math.factorial(string)*math.factorial(string))))
