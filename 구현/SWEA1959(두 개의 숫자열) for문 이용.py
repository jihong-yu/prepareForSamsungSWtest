T = int(input())

for order in range(T):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    if N > M:
        Ai, Bj = Bj, Ai
        N, M = M, N

    result = []
    for i in range(M - N + 1):
        temp = []
        for j in range(N):
            temp.append(Ai[j] * Bj[i + j])
        result.append(sum(temp))

    print(f'#{order + 1} {max(result)}')