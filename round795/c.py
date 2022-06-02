# for i in range(2 ** 20):
#     S = ''
#     for j in range(20):
#         if i >> j & 1:
#             S += '1'
#         else:
#             S += '0'
#     tmp = 0
#     cnt = 0
#     for s in S:
#         if s == '1':
#             cnt += 1
#     if cnt == 15:
#         for i in range(19):
#             tmp += int(S[i:i+2])
#         print(S, tmp)


T = int(input())
ans = []
for _ in range(T):
    N, K = map(int, input().split())
    S = input()
    idxs = []
    cnt = 0
    for i in range(N):
        if S[i] == '1':
            idxs.append(i)
            cnt += 1
    if len(idxs) >= 2:
        if idxs[0] + N - idxs[-1] - 1 <= K:
            ans.append(11 * (cnt - 1))
        elif N - idxs[-1] - 1 <= K:
            ans.append(11 * (cnt - 1) + 1)
        elif idxs[0] <= K:
            ans.append(11 * cnt - 1)
        else:
            ans.append(11 * cnt)
    elif len(idxs) == 1:
        if N - idxs[0] - 1 <= K:
            ans.append(1)
        elif idxs[0] <= K:
            ans.append(10)
        else:
            ans.append(11)
    else:
        ans.append(0)
print(*ans, sep='\n')
