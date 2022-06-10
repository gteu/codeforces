T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    m = max([A[i] - B[i] for i in range(N)])
    flg = True
    for i in range(N):
        if A[i] < B[i] or (A[i] - B[i] < m and B[i] != 0):
            flg = False
    if flg:
        print('YES')
    else:
        print('NO')
