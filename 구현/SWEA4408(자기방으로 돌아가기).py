import sys

sys.stdin = open('input.txt', 'r')


def my_max(array):
    max_ = array[0]
    for i in array:
        if max_ < i:
            max_ = i
    return max_


T = int(input())
for order in range(1, T + 1):

    N = int(input())
    array = []
    for i in range(N):
        a, b = map(int, input().split())
        if a % 2:  # 홀수라면
            a += 1  # (1,2),(3,4)...가 똑같기 때문에 +1 해준다.
        if b % 2:  # 홀수라면
            b += 1  # (1,2),(3,4)...가 똑같기 때문에 +1 해준다.
        if a > b:  # 만약 더 큰방에서 작은방으로 갈 경우 a,b를 다시 바꿔준다.
            a, b = b, a
        array.append([a, b])

    hallway = [0] * 401  # 복도를 만든다.
    count = 0
    for i in range(N):  # 입력받은 N을 돌면서
        for j in range(array[i][0], array[i][1] + 1):  # 출발 방부터 도착방까지 이동 동선을 기록
            hallway[j] += 1

    print(f'#{order} {my_max(hallway)}')
