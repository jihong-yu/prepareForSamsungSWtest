for _ in range(1, 10 + 1):
    order = int(input())
    array = []
    for _ in range(100):
        array.append(list(map(int, input().split())))

    result = []  # 모든 합들을 모아놓을 리스트

    sum_rightup = 0  # 오른쪽위 대각선 합
    sum_rightdown = 0  # 오른쪽아래 대각선 합
    for i in range(100):
        sum_width = 0  # 가로합을 저장할 리스트
        sum_height = 0  # 세로합들을 저장할 리스트
        for j in range(100):
            sum_width += array[i][j]  # 가로합 더해준다.
            sum_height += array[j][i]  # 세로합 더해준다.
            if i == j:  # 만약 두개의 인덱스가 같다면(오른쪽아래 대각선합)
                sum_rightup += array[i][j]
            if i + j == 99:  # 만약 두개의 합이 99라면(오른쪽위 대각선합)
                sum_rightdown += array[i][j]
        result.append(sum_width)
        result.append(sum_height)

    result.append(sum_rightup)
    result.append(sum_rightdown)
    print(f'#{order} {max(result)}')  # 최댓값 출력
