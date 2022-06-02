T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    ans.append(A[sum(B) % N])
print(*ans, sep='\n')
