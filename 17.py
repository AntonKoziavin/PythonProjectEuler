ten0 = 36                                                           # От 1 до 9
ten1 = 3+6+6+8+8+7+7+9+8+8                                          # От 10 до 19
hundred = ten0 + ten1                                               # От 1 до 19
hundred += ten0*8 + 60 + 60 + 50 + 50 + 50 + 70 + 60 + 60           # От 20 до 99
print(hundred)
count = hundred
count += hundred + 13*99 + 10                                       # От 101 до 199 + 100
count += hundred + 13*99 + 10                                       # От 201 до 299 + 200
count += hundred + 15*99 + 12
count += hundred + 14*99 + 11
count += hundred + 14*99 + 11
count += hundred + 13*99 + 10
count += hundred + 15*99 + 12
count += hundred + 15*99 + 12
count += hundred + 14*99 + 11 + 11                                  # От 901 до 999 + 900 + 1000
print(count)
