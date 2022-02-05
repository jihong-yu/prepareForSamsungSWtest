T = int(input())

for i in range(1, T + 1):
    N, K = map(int, input().split())
    K_list = list(map(int, input().split()))
    students = list(map(int, range(1, N + 1)))
    result = []  # 제출하지 않은 명단을 저장할 리스트
    for j in students:  # 학생 1~N 중에
        if j not in K_list:  # 만약 제출한 명단에 없다면
            result.append(j)  # 그 사람을 출력 리스트에 추가
    print(f'#{i}', end=" ")
    print(*result)  # 언패킹 연산자를 이용해 출력
