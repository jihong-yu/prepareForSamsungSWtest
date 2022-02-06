for order in range(1, 10 + 1):

    length = int(input())
    array = []
    for _ in range(100):
        array.append(list(map(int, input().split())))

    count = 0  # 결과를 출력할 변수
    for i in range(100):
        temp = []  # 자석들을 담을 리스트
        for j in range(100):
            if array[j][i] != 0:  # 만약 0이 아니라면(자석이 있다면)
                temp.append(array[j][i])  # 그 자석들을 임시리스트에 넣어준다.

        for left in range(len(temp)):  # 왼쪽부터 돌면서 2자석은 다 0으로 바꿔준다.
            if temp[left] == 2:
                temp[left] = 0
            else:  # 단 1을 만나면 종료
                break

        for right in range(len(temp) - 1, -1, -1):  # 오른쪽부터 돌면서 1자석은 다 0으로 바꿔준다.
            if temp[right] == 1:
                temp[right] = 0
            else:  # 단 2를 만나면 종료
                break
        gyochak = []  # 교착상태를 담을 임시 리스트선언
        for k in range(len(temp)):  # 자석개수를 돈다.
            if temp[k] != 0:  # 만약 0이 아니라면(앞뒤로 테이블밑으로빠진 자석들은 무시)
                if k != len(temp) - 1 and temp[k] != temp[k + 1]:  # 만약 마지막 인덱스가 아니고 두개의 리스트원소가 다르다면
                    gyochak.append(temp[k])
                if k == len(temp) - 1:  # 마지막 인덱스 이면서 0이 아니라면 무조건 담아준다.
                    gyochak.append(temp[k])
            if len(gyochak) == 2:  # 만약 2개가 담겼다면(1,2) 교착상태이므로
                count += 1  # 개수를 1개 추가해준다.
                gyochak = []  # 그 후 다시 리스트를 비워준다.
    print(f'#{order} {count}')
