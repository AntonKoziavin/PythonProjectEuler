spis = list()
poly = list()
for a in range(100, 1000):
    for b in range(100, 1000):
        number = a * b
        if len(str(number)) == 6:
            for i in str(number):
                spis.append(i)
                if len(spis) == 6:
                    if spis[0] == spis[-1]:
                        if spis[1] == spis[-2]:
                            if spis[2] == spis[-3]:
                                poly.append(number)
                    spis.clear()
print(max(poly))