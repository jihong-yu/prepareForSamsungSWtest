for order in range(1, 10 + 1):
    n = int(input())
    gangnam = list(map(int, input().split()))
    count = 0  # 정답을 출력할 변수
    for i in range(2, len(gangnam) - 2):  # 초기 양쪽 2개씩 0을 제외한 인덱스를 돈다.
        max_result = []  # i를 기준으로 양쪽 2개씩 총4개의 조망권을 저장할 리스트 선언
        for j in range(i - 2, i + 3):  # 양쪽으로 2번씩 돈다.
            if i == j:  # 만약 인덱스가 본인이라면 밑에 조건을 실행할 필요가 없으므로 continue
                continue
            result = gangnam[i] - gangnam[j]  # 우선 조망권을 받을 수 있는 층수를 계산하여
            if result < 0:  # 그 값이 음수라면 조망권이 확보된 집이 없으므로
                max_result = []  # 리스트를 다시 비워주고
                break  # 반복문 탈출
            max_result.append(result)  # 조망권 값들을 리스트에 추가해준다.

        if max_result:  # 만약 리스트가 비어있지 않다면
            count += min(max_result)  # 조망권 확보가 가능한 최솟값을 출력변수에 더해준다.

    print(f'#{order} {count}')
