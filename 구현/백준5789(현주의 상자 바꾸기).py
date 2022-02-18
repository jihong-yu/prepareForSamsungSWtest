import sys

sys.stdin = open('input.txt', 'r')
T = int(input())
for order in range(1, T + 1):
    N, Q = map(int, input().split())
    array = [0 for x in range(N + 1)]
    for i in range(1, Q + 1):  # Q의 횟수만큼
        L, R = map(int, input().split())  # L,R을 입력 받는다.

        for j in range(L, R + 1):  # L,R의 범위만큼 i값으로 바꿔준다.
            array[j] = i

    print(f'#{order}', *array[1:])  # 인덱스 0일때를 제외하고 출력한다.