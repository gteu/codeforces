import math


def get_divisor(x):
    divisor = []
    for i in range(1, int(pow(x, 0.5)) + 1):
        if x % i == 0:
            divisor.append(i)
            if i != x//i:
                divisor.append(x // i)

    return divisor


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = input()
    P = list(map(int, input().split()))
    groups = []
    used = set()
    for i in range(N):
        if i in used:
            continue
        group = []
        cur = i
        while cur not in used:
            group.append(cur)
            used.add(cur)
            cur = P[cur] - 1
        groups.append(group)
    A = []
    for group in groups:
        tmpS = ''
        for i in group:
            tmpS += S[i]
        L = len(group)
        D = get_divisor(L)
        D.sort()
        for d in D:
            ref = tmpS[:d]
            flg = True
            for i in range(L // d):
                if tmpS[d * i:d * i + d] != ref:
                    flg = False
            if flg:
                A.append(d)
                break
    lcm = A[0]
    for a in A:
        lcm = a * lcm // math.gcd(a, lcm)
    ans.append(lcm)
print(*ans, sep='\n')
