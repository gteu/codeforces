T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = input()
    c = S[:K].count('B')
    m = c
    for i in range(N - K):
        if S[i] == 'B':
            c -= 1
        if S[i + K] == 'B':
            c += 1
        m = max(m, c)
    print(K - m)
