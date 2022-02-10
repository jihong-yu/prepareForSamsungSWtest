# import sys

# sys.stdin = open('input.txt', 'r')

T = int(input())

for order in range(1, T + 1):

    N = int(input())
    array = [list(map(int, input())) for _ in range(N)]
    mid_idx = (N // 2)  # 중앙 인덱스를 설정해준다.
    sum_ = 0  # 합을 출력할 변수 선언

    # 행을 기준으로 0부터 ~ 절반까지 돈다.
    for i in range((N // 2) + 1):
        sum_ += array[i][mid_idx]  # 중앙값은 무조건 + 해준다.
        for j in range(1, i + 1):  # 그 후 현재 행의 인덱스 만큼 양옆으로 가면서 더해준다.
            sum_ += array[i][mid_idx - j]
            sum_ += array[i][mid_idx + j]

    # 행을 역으로 끝 부터 ~ 절반 전까지 돈다.
    for i in range(N - 1, N // 2, -1):
        sum_ += array[i][mid_idx]  # 중앙값은 무조건 + 해준다.
        for j in range(1, N - i):  # 그 후 (전체 길이 - 현재 행의 인덱스 + 1) 만큼 양옆으로 가면서 더해준다.
            sum_ += array[i][mid_idx - j]
            sum_ += array[i][mid_idx + j]

    print(f'#{order} {sum_}')
