from collections import Counter

T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    mA = Counter(A).most_common()[0]
    if mA[1] >= 3:
        ans.append(mA[0])
    else:
        ans.append(-1)
print(*ans, sep='\n')
