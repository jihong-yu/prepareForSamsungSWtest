for _ in range(1, 10 + 1):
    order = int(input())
    data = []
    break_check = False  # 만약 2와 연결된 출발점을 찾았다면 전체 반복문을 탈출할 변수
    for _ in range(100):
        data.append(list(map(int, input().split())))

    for x in range(100):  # 0~99 까지 돈다.
        if data[0][x] != 1:  # 만약 출발지 x가 1이 아니라면 continue
            continue
        i = 0  # 행 변수 i
        j = x  # 열 변수 j는 시작열인 x로 초기화
        left_to_right = True  # 현재 이동이 왼쪽에서 오른쪽으로 진행되고 있는지를 체크하는 변수
        right_to_left = True  # 현재 이동이 오른쪽에서 왼쪽으로 진행되고 있는지 체크하는 변수
        while True:

            if i == len(data) - 1:  # 만약 마지막 행까지 왔다면 break
                break

            if data[i + 1][j] == 2:  # 만약 다음 행의 수가 2라면 도착했으므로
                print(f'#{order} {x}')  # 출력 후
                break_check = True  # 전체 반복문 탈출을 위해 True로 바꿔준 후
                break  # 탈출

            # 만약 열이 마지막열이 아니고 오른쪽 열이 1이고 현재 왼쪽에서 오는 중이라면
            if j != len(data) - 1 and data[i][j + 1] == 1 and left_to_right == True:
                right_to_left = False  # 다시 오른쪽에서 왼쪽으로 가면 안되기 때문에 right변수는 True로 해주고
                j += 1  # 열을 한칸 이동
                
            # 만약 열 인덱스가 0이 아니고 왼쪽 열이 1이고 현재 오른쪽에서 오는 중이라면
            elif j != 0 and data[i][j - 1] == 1 and right_to_left == True:
                left_to_right = False  # 다시 왼쪽에서 오른쪽으로 가면 안되기 때문에 True로 바꿔준 후
                j -= 1  # 열을 한칸 왼쪽으로 땡긴다.

            # 만약 양옆이 0이고 아래가 1이라면
            elif data[i + 1][j] == 1:
                right_to_left = True  # 다시 양옆으로 이동할 수 있으므로 False로 바꿔준다.
                left_to_right = True  # 다시 양옆으로 이동할 수 있으므로 False로 바꿔준다.
                i += 1  # 열을 한칸 증가.

        if break_check:  # 만약 탈출 변수가 True로 바꼇다면
            break  # 전체반복문 탈출
