array = [list(map(int, input().split())) for x in range(4)]

result = 0
for i in range(1, 101):  # 1,1 ~ 100,100 까진돈다.
    for j in range(1, 101):  # 1,1 ~ 100,100 까지 돈다.
        for k in range(4):  # 입력 받은 직사각형 4개를 돈다.
            # 만약, 1,1 ~ 100,100 까지 도는데 해당 좌표가 직사각형의 좌표안에 포함되어 있으면 넓이 1을 더해주고
            # 더이상 직사각형 안에 속하는지 검사안해도 되기 때문에 반복문 탈출
            if array[k][0] < i <= array[k][2] and array[k][1] < j <= array[k][3]:
                result += 1
                break

print(result)