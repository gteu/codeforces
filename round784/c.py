T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ref = A[0] % 2
    flag = True
    for a in A[::2]:
        if a % 2 != ref:
            flag = False

    ref = A[1] % 2
    for a in A[1::2]:
        if a % 2 != ref:
            flag = False

    if flag:
        print('YES')
    else:
        print('NO')
