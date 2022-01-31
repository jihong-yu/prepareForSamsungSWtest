C, R = map(int, input().split())
K = int(input())
array = [[0] * C for _ in range(R)]

i = 0  # 행 변수
j = 0  # 열 변수
a = 0  # 대기번호를 저장할 변수
cycle = 0  # 4가지 cycle(위로,오른쪽으로,아래로,왼쪽으로)중 어느 cycle에 위치하는지 표기

col_limit_up = C - 1  # 최대 열로 갈 수 있는 인덱스
row_limit_up = R - 1  # 최대 행으로 갈 수 있는 인덱스
col_limit_down = 1  # 최소 열로 갈 수 있는 열 인덱스
row_limit_down = 0  # 최소 행으로 갈 수 있는 행 인덱스
while True:

    if a == C * R:  # 만약 대기번호가 끝 번호라면
        break  # 반복문 탈출

    if cycle == 0:  # cycle이 0번일 때는 위로 올라간다.
        while True:
            a += 1  # 대기 번호 1증가
            array[i][j] = a  # 대기 번호를 대입
            if i == row_limit_up:  # 만약 행이 최대 행으로 갈 수 있는 인덱스에 도달했다면
                row_limit_up -= 1  # 그 최대행을 다음번에 도달할때는 한칸 앞당겨지기 때문에  -1 해준다.
                j += 1  # 다음 cycle(오른쪽) 시작할 때는 한칸 열을 움직인 상태에서 시작해야 하기 때문에 열 인덱스 +=1
                break  # 탈출
            i += 1  # 행을 계속해서 +1 씩 해준다.

    elif cycle == 1:  # 1번일 때는 오른쪽으로 간다.
        while True:
            a += 1  # 대기 번호 1증가
            array[i][j] = a  # 대기 번호를 대입
            if j == col_limit_up:  # 만약 열이 최대 열로 갈 수 있는 인덱스에 도달했다면
                col_limit_up -= 1  # 그 최대열을 다음번에 도달할때는 한칸 앞당겨지기 때문에 -1 해준다.
                i -= 1  # 다음 cycle(아래쪽) 시작할 때는 한칸 행을 아래쪽으로 한칸 움직인 상태에서 시작해야 하기 때문에 행 인덱스 -=1
                break  # 탈출
            j += 1  # 열을 계속해서 +1 해준다.

    elif cycle == 2:  # cycle이 2번일 때는 아래로 내려간다.
        while True:
            a += 1  # 대기 번호 1증가
            array[i][j] = a  # 대기 번호를 대입
            if i == row_limit_down:  # 만약 행이 최소 열로 갈 수 있는 인덱스에 도달했다면
                row_limit_down += 1  # 그 최소 행을 다음번에 도달할때는 한칸 앞당겨지기 때문에 +1 해준다.
                j -= 1  # 다음 cycle(왼쪽) 시작할 때는 열을 왼쪽으로 한칸 움직인 상태에서 시작해야 하기 때문에 열 인덱스 -=1
                break  # 탈출
            i -= 1  # 행을 계속해서 -1 해준다.

    elif cycle == 3:  # cycle이 3번일 때는 왼쪽으로 간다.
        while True:
            a += 1  # 대기 번호 1증가
            array[i][j] = a  # 대기 번호를 대입
            if j == col_limit_down:  # 만약 열이 최소 열로 갈 수 있는 인덱스에 도달했다면
                col_limit_down += 1  # 그 최소 열을 다음번에 도달할때는 한칸 앞당겨지기 때문에 +1 해준다.
                i += 1  # 다음 cycle(위쪽) 시작할 때는 행을 위쪽으로 한칸 움직인 상태에서 시작해야 하기 때문에 행 인덱스 +=1
                break  # 탈출
            j -= 1  # 열을 계속해서 -1씩 당겨준다.

    cycle = (cycle + 1) % 4  # cycle이 0~3 으로 반복되게 하기 위해서 4의 나머지로 돌려준다.

for i in range(len(array)):  # 배열 길이 만큼돈다.
    if array[i].count(K) == 1:  # 만약 해당 대기번호가 있따면
        print(array[i].index(K) + 1, i + 1)  # 그 배열 K의 열 인덱스구해서 +1, 행 인덱스 + 1
        exit()  # 코드 종료

print(0)  # 위에서 코드종료가 안되면 0을 출력
