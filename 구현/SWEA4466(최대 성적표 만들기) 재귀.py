T = int(input())


def solution(depth, step):
    global result

    if depth == K:
        if result < sum(sum_):
            result = sum(sum_)
            return
        else:
            return

    for i in range(step, N):
        sum_.append(total[i])
        solution(depth + 1, i + 1)
        sum_.pop()


for order in range(1, T + 1):
    N, K = map(int, input().split())
    total = list(map(int, input().split()))
    sum_ = []
    result = 0
    solution(0, 0)
    print(f'#{order} {result}')
