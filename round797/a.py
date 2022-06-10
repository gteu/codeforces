T = int(input())
for _ in range(T):
    N = int(input())
    base_h = (N - 3) // 3
    if N % 3 == 2:
        print(base_h + 2, base_h + 3, base_h)
    elif N % 3 == 1:
        print(base_h + 1, base_h + 3, base_h)
    else:
        print(base_h + 1, base_h + 2, base_h)
