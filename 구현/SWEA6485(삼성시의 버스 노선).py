import sys

# sys.stdin = open('input.txt', 'r')

T = int(input())

for order in range(1, T + 1):
    N = int(input())  # 노선의 수
    nosun = []  # 노선의 정보를 담을 리스트

    for i in range(N):
        nosun.append(list(map(int, input().split())))  # 노선의 정보 입력

    P = int(input())  # 정류장의 개수
    C = []  # 정류장의 번호
    info = {}  # 딕셔너리에 정류장번호 : 지나가는 횟수 형식으로 저장
    for i in range(P):
        station = int(input())
        C.append(station)
        info[station] = 0

    for i in nosun:  # 노선의 정보를 돈다.
        for j in range(i[0], i[1] + 1):  # 노선의 첫번째부터 끝 정류장까지 돈다.
            if j in info:  # 만약 입력받은 정류장이 존재하만다면
                info[j] += 1  # 지난가는 횟수를 1회 증가

    print(f'#{order}', end=" ")
    for i in C:  # 입력받은 정류장을 순회하며 저장된 횟수 출력
        print(info[i], end=" ")
    print()
