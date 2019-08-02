def show_numbers(limit):
    x = limit + 1
    b = range(0, x)
    for i in b:
        if i % 2 == 0:
            print(f'{i}-even')
        else:
            print(f'{i}-odd')
    return i






message = int(input('Upto: '))
print(show_numbers(message))


