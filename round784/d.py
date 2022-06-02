T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = input()

    flag = True
    for s in S.split('W'):
        if s == '':
            continue
        if all([c == 'B' for c in s]) or all([c == 'R' for c in s]):
            flag = False

    if flag:
        ans.append('YES')
    else:
        ans.append('NO')

print(*ans, sep='\n')
