T = int(input())

for order in range(1, T + 1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]

    result = []  # 개수를 담아 놓을 리스트 선언

    for a in range(n):
        for b in range(n):  # 이중 리스트의 모든 인덱스를 시작지점으로 정한다.
            raw_count = 0  # 행 개수를 저장할 변수
            for i in range(a, n):  # 시작지점 행부터 시작
                if array[i][b] == 0:  # 만약 해당지점이 0이라면 조사할 필요가 없으므로 바로 break
                    break
                raw_count += 1  # 0이 아니라면 행렬 시작이므로 열개수를 1개 증가
                column_count = 0  # 열 개수를 세어줄 변수 선언
                for j in range(b, n):  # 시작지점 열 조사

                    if j != n - 1 and array[i][j + 1] != 0:  # 만약 마지막열이 아니고 다음 열이 0이아니라면
                        column_count += 1  # 열개수 증가
                        array[i][j] = 0  # 조사 했기 때문에 해당 열의 값을 0으로 바꿔준다.(다음 조사때 조사를안하기위해서)
                    elif j != n - 1 and array[i][j + 1] == 0:  # 만약 마지막열이 아니고 다음 열이 0이라면
                        column_count += 1  # 열개수 증가
                        array[i][j] = 0  # 조사 했기 때문에 해당 열의 값을 0으로 바꿔준다.(다음 조사때 조사를안하기위해서)
                        break
                    elif j == n - 1:  # 위의 조건을 충족하면서 만약 마지막 열이라면
                        column_count += 1  # 열 개수 증가
                        array[i][j] = 0  # 조사 했기 때문에 해당 열의 값을 0으로 바꿔준다.(다음 조사때 조사를안하기위해서)

            if raw_count * column_count != 0:  # 만약 열개수나 행개수가 0이 아니라면 행렬이 존재한다는 의미이므로
                result.append([raw_count * column_count, raw_count, column_count])  # 해당 정보 추가.

    result.sort(key=lambda x: (x[0], x[1]))  # 우선 크기대로 오름차순 정렬한 뒤 행 개수로 오름차순 정렬해준다.

    temp = []  # 출력할 변수 선언
    for r in result:  # 행렬정보가 있는 리스트를 돈다.
        temp.append(r[1])  # 행 추가
        temp.append(r[2])  # 열 추가
    print(f'#{order} {len(temp) // 2}', end=" ")
    print(*temp)
