def battery_charge(n):
    bar = round(n / 10)
    level = '❚'
    final = []
    for x in range(bar):
        final.append(level)
    if len(final) < 10:
        for x in range(len(final), 10):
            final.append(' ')
    print('[', end='')
    for x in final:
        print(f"{x}", end='')
    print(']', end='')
    print()
    print(f"{n}%")

battery_charge(50)