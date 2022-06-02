from collections import defaultdict
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(list)
    flg = True
    tmp = [-1] * N
    for i, a in enumerate(A):
        d[a].append(i)

    for k, v in d.items():
        if len(v) == 1:
            flg = False
        else:
            for i in range(len(v)):
                tmp[v[i]] = v[(i + 1) % len(v)]

    if flg:
        print(*list(map(lambda x: x + 1, tmp)))
    else:
        print(-1)
