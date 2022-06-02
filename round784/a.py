T = int(input())
for _ in range(T):
    N = int(input())
    if N >= 1900:
        print('Division', 1)
    elif N >= 1600:
        print('Division', 2)
    elif N >= 1400:
        print('Division', 3)
    else:
        print('Division', 4)
