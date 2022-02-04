T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    paris = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0  # 최대 합 저장할 변수
    start_c = 0  # 열 인덱스 저장할 변수
    start_r = 0  # 행 인덱스 저장할 변수
    break_ = False  # 반복문 탈출 여부 체킹
    while True:
        count = 0  # 잡은 파리 횟수를 저장할 변수
        r = start_r  # 시작행 인덱스 저장할 변수
        c = start_c  # 시작열 인덱스 저장할 변수
        sum_array = []  # 합을 구할 리스트
        while True:  # 반복문을 돈다.
            if start_c > N - M:  # 만약 시작 열 인덱스가 뽑아야할 양보다 더 크다면
                start_r += 1  # 다음 행을 돌아야 하므로 시작행 인덱스를 +1 해주고
                start_c = 0  # 다음행의 첫번째 열부터 다시 돌아야하므로 열 시작번호를 0으로 맞춰준다.
                break  # 그 후 탈출
            if start_r > N - M:  # 만약 시작 행 인덱스가 뽑아야할 양보다 더 크다면
                break_ = True  # 더이상 돌 필요가 없으므로 탈출변수인 break_ 값을 True로 바꿔주고 탈출한다.
                break
            sum_array.append(paris[r][c])  # 위의 조건에 부합하지 않는다면 해당 파리를 잡는다.
            c += 1  # 그 다음 열로 이동
            count += 1  # 잡은 파리 개수도 1개 추가
            if count == M:  # 만약 횟수가 M번이라면(즉 한 행에서 M번 잡았다면 다음 열로 넘어가야 하므로)
                count = 0  # 그 횟수를 0으로 바꿔주고
                r += 1  # 열을 한칸 이동시킨다.
                c = start_c  # 그 후 처음에 시작했던 열번호를 대입해준다.
            if len(sum_array) == M * M:  # 만약 잡은 파리가 M * M 번이 되었다면
                if max_sum < sum(sum_array):  # 그 합을 비교해서 더크다면
                    max_sum = sum(sum_array)  # 그 값을 최대값으로 바꿔주고
                start_c += 1  # 그 다음열부터 다시 파리를 잡기 위해 시작열 번호를 +1 해준다.
                break  # 그 후 탈출
        if break_:  # 만약 탈출 체킹 변수가 True로 바꼈다면
            print(f'#{i} {max_sum}')  # 그 최대 합을 출력한 후
            break  # 종료
