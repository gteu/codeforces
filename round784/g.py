T = int(input())
ans = []
for _ in range(T):
    N, M = map(int, input().split())
    S = []
    for _ in range(N):
        S.append(input())
    ret = []
    for j in range(M):
        new = []
        dot_cnt = 0
        stone_cnt = 0
        for i in range(N):
            if S[i][j] == '.':
                dot_cnt += 1
            elif S[i][j] == '*':
                stone_cnt += 1
            elif S[i][j] == 'o':
                new += ['.'] * dot_cnt + ['*'] * stone_cnt + ['o']
                dot_cnt, stone_cnt = 0, 0

        new += ['.'] * dot_cnt + ['*'] * stone_cnt + ['o']
        ret.append(''.join(new))
    for i in range(N):
        tmp = ''
        for j in range(M):
            tmp += ret[j][i]
        ans.append(tmp)
print(*ans, sep='\n')
