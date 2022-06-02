T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    r = N - 1
    ls, rs = 0, 0
    ret = 0
    for l in range(N):
        ls += A[l]
        while ls >= rs + A[r] and r > 0:
            rs += A[r]
            r -= 1
        if ls == rs and l <= r:
            ret = N - r + l
    ans.append(ret)
print(*ans, sep='\n')
