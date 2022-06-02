from collections import defaultdict


def solve():
    N = int(input())
    d = defaultdict(int)
    for _ in range(N):
        S = input()
        d[S] += 1
    ret = 0
    for k1, v1 in d.items():
        for k2, v2 in d.items():
            if (k1[0] == k2[0] and k1[1] != k2[1]) or (k1[0] != k2[0] and k1[1] == k2[1]):
                ret += v1 * v2
    ret //= 2
    ans.append(ret)


T = int(input())
ans = []
for _ in range(T):
    solve()
print(*ans, sep='\n')
