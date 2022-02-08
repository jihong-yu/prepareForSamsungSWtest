T = int(input())

for order in range(1, T + 1):
    N, K = map(int, input().split())
    total = list(map(int, input().split()))
    total.sort(reverse=True)
    result = 0
    for i in range(K):
        result += total[i]

    print(f'#{order} {result}')