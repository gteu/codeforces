T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    even = 0
    for a in A:
        if a % 2 == 0:
            even += 1
    print(min(N - even, even))
