import sys

sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    result = [0] * (1000 + 1)  # 개수를 셀 리스트 선언

    for i in info:
        if i[1] > i[2]:
            i[1], i[2] = i[2], i[1]

        if i[0] == 1:
            for a in list(range(i[1], i[2] + 1)):
                result[a] += 1
        elif i[0] == 2:
            for a in list(range(i[1], i[2], 2)) + [i[2]]:
                result[a] += 1
        else:
            if i[1] % 2 == 0:
                for a in list(x for x in range(i[1], i[2]) if x % 4 == 0) + [i[2]]:
                    result[a] += 1
            else:
                for a in list(x for x in range(i[1], i[2]) if x % 3 == 0 and x % 10 != 0) + [i[2]]:
                    result[a] += 1

    print(f'#{tc} {max(result)}')
