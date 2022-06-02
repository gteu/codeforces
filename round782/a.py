T = int(input())
for _ in range(T):
    N, R, B = map(int, input().split())
    S = []
    q = R // (B + 1)
    r = R % (B + 1)
    cnt = 0
    for i in range(B + 1):
        if cnt < r:
            S += ['R'] * (q + 1)
            S += ['B']
            cnt += 1
        else:
            S += ['R'] * q
            S += ['B']
    print(''.join(S)[:N])
