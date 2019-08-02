def prime_num(limit):
    key = []
    t = key[0:-1]
    nill = []
    for i in range(limit):
        key.append(i)
        for lol in key:
            if not lol % t == 0:
                nill.append(lol)
    print(nill)


message = int(input('upto: '))
print(prime_num(message))