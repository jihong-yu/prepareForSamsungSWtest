T = int(input())

for order in range(1, T + 1):
    N, M = map(int, input().split())
    russia = [list(map(str, input())) for _ in range(N)]
    result = N * M  # 바꿔야되는 횟수 저장(초기값을 최대값으로 저장)
    one_count = 0  # W로 만들기위해 칠해야 하는 개수
    for w in range(0, N - 2):  # 맨마지막 B,R을 칠해야하는 2개의 행 전까지 반복문을 돈다.
        for k1 in range(0, M):  # 가로로 M까지돈다.
            if russia[w][k1] != 'W':  # 만약 W가 아니라면
                one_count += 1  # 지워야 되는 횟수 +1
        two_count = 0  # B로 만들기위해 칠해야 하는 개수
        if result <= one_count:  # 만약 저장되어있는 횟수보다 이미 크다면
            break  # 탈출
        for b in range(1 + w, N - 1):  # 위에서 칠한 행(W) 그 다음부터 마지막R을 칠해야하는 행을 제외한 행까지 돈다.
            for k2 in range(0, M):  # 가로로 M까지 돈다.
                if russia[b][k2] != 'B':  # 만약 B가 아니라면
                    two_count += 1  # 칠해야하는 횟수 +1
            if result <= one_count + two_count:  # 만약 이미 두개의 합이 저장되어있는 값보다 크거나 같다면
                break  # 탈출
            three_count = 0  # R로 만들기위해 칠해야 하는 개수
            for r in range(1 + b, N):  # 위에서 칠한 행(B) 그 다음부터 마지막 행까지 돈다.
                for k3 in range(0, M):  # 가로로 M까지 돈다.
                    if russia[r][k3] != 'R':  # 만약 R이 아니라면
                        three_count += 1  # 횟수 +1
            if result > (one_count + two_count + three_count):  # 다 돌고나서 만약 셋의 합이 저장되어있는 횟수보다 작다면
                result = (one_count + two_count + three_count)  # 그 값을 최솟값으로 변경

    print(f'#{order} {result}')
