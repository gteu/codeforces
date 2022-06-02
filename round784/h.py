T = int(input())
ans = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ret = 0
    for i in reversed(range(31)):
        cnt = 0
        for a in A:
            if a & (2 ** i) > 0:
                cnt += 1
        if cnt == N:
            ret += 2 ** i
        elif N - cnt <= K:
            K -= (N - cnt)
            ret += 2 ** i
    ans.append(ret)
print(*ans, sep='\n')
