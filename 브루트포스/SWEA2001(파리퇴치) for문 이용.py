T = int(input())

for a in range(1, T + 1):
    N, M = map(int, input().split())
    paris = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0  # 최대 합 저장할 변수
    for i in range(N):
        if i + M > N:
            break
        for j in range(N):
            sum_array = []
            if j + M > N:
                break
            for k in range(i, i + M):
                for h in range(j, j + M):
                    sum_array.append(paris[k][h])
            if max_sum < sum(sum_array):
                max_sum = sum(sum_array)
    print(f'#{a} {max_sum}')