T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    if max(A) >= max(B):
        ans.append('Alice')
    else:
        ans.append('Bob')
    if max(B) >= max(A):
        ans.append('Bob')
    else:
        ans.append('Alice')

print(*ans, sep='\n')
