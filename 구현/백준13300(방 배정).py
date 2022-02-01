N, K = map(int, input().split())
# 각각의 학년에 array[i]에 array[i][0] = 여학생의 수 array[i][1] = 남학생의 수를 저장하기 위핸 이차원리스트 선언
array = [[0, 0] for _ in range(6)]
for i in range(N):
    gender, grade = map(int, input().split())  # 0 - 여자 1- 남자
    array[grade - 1][gender] += 1  # 해당 이차원 리스트의 학년에 해당 성을 가진 사람수 1명씩 추가.

count = 0  # 횟수를 셀 변수 선언
for i in range(len(array)):
    for j in range(len(array[i])):
        count += (array[i][j] // K)  # 우선 몫을 대입한 후
        if array[i][j] % K > 0:  # 만약 나머지가 1명이상이라면 방이 한개 더 필요하기 때문에
            count += 1  # 방 개수를 1개더 추가해준다.

print(count)
