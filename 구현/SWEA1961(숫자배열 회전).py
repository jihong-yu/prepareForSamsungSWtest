T = int(input())


def solution(order, array, N):
    result = []
    for i in range(N):
        b = ""
        for j in range(N - 1, -1, -1):
            b += str(array[j][i])
        result.append(b)

    for i in range(N - 1, -1, -1):
        b = ""
        for j in range(N - 1, -1, -1):
            b += str(array[i][j])
        result.append(b)

    for i in range(N - 1, -1, -1):
        b = ""
        for j in range(N):
            b += str(array[j][i])
        result.append(b)

    print(f'#{order}')
    for i in range(N):
        for j in range(i, N * 3, N):
            print(result[j], end=" ")
        print()


for order in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    solution(order, array, N)
