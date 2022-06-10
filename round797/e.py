T = int(input())
ans = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ret = 0
    mod = []
    for a in A:
        ret += a // K
        mod.append(a % K)
    mod.sort()
    r = N - 1
    for l in range(N):
        if l >= r:
            break
        if mod[l] + mod[r] >= K:
            ret += 1
            r -= 1
    ans.append(ret)
print(*ans, sep='\n')
