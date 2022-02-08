T = int(input())


def solution(order):
    # 작은 사각형 3 x 3 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check_square = set()
            for k in range(i, i + 3):
                for h in range(j, j + 3):
                    check_square.add(array[k][h])
            if len(check_square) != 9:
                print(f'#{order} {0}')
                return

    # 전체 가로줄,세로줄 검사
    for i in range(9):
        check_list_r = set()
        check_list_c = set()
        for j in range(9):
            check_list_r.add(array[i][j])
            check_list_c.add(array[j][i])

        if len(check_list_r) != 9 or len(check_list_c) != 9:
            print(f'#{order} {0}')
            return
    # 만약 위에서 return 되지 않았다면 숫자가 겹치지 않는다는 것
    print(f'#{order} {1}')


for order in range(1, T + 1):
    array = [list(map(int, input().split())) for _ in range(9)]

    solution(order)
