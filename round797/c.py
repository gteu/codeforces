T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    F = list(map(int, input().split()))
    D = [0] * N
    D[0] = F[0] - S[0]
    for i in range(1, N):
        if S[i] >= F[i - 1]:
            D[i] = F[i] - S[i]
        else:
            D[i] = F[i] - F[i - 1]
    ans.append(D)
for i in range(T):
    print(*ans[i])
