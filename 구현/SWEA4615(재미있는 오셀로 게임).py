import sys

sys.stdin = open('input.txt', 'r')
T = int(input())
for order in range(1, T + 1):
    N, M = map(int, input().split())  # 가로, 세로

    board = [[0] * N for _ in range(N)]  # 보드판을 0으로 초기화
    # 초기에 보드판의 중앙에 4개의 돌을 놓아준다.
    for r in range(N // 2 - 1, N // 2 + 1):
        for c in range(N // 2 - 1, N // 2 + 1):
            if r == c:
                board[r][c] = 2
            else:
                board[r][c] = 1
    for _ in range(M):
        c, r, color = map(int, input().split())
        board[r - 1][c - 1] = color  # 보드판의 입력이 열,행 순으로 주어지므로 행,열 및 인덱스로 바꿔준다.

        dx = [-1, -1, 0, +1, +1, +1, 0, -1]  # 행이동: 위 오른쪽위 오른쪽 오른쪽아래 아래 왼쪽아래 왼쪽 왼쪽위
        dy = [0, +1, +1, +1, 0, -1, -1, -1]  # 열이동: 위 오른쪽위 오른쪽 오른쪽아래 아래 왼쪽아래 왼쪽 왼쪽위
        now_dx, now_dy = r - 1, c - 1  # 현재 위치를 저장해준다.
        for i in range(8):  # 모든 방향을 이동해준다.
            new_dx = now_dx + dx[i]  # 각 방향으로 이동(새로운*1 돌이라고칭함) 즉, 바로 옆에 붙어있는 돌위치
            new_dy = now_dy + dy[i]  # 각 방향으로 이동(새로운*1 돌이라고칭함) 즉, 바로 옆에 붙어있는 돌위치

            # 만약 그 방향이 범위를 벗어난다면 continue
            if new_dx >= N or new_dx < 0 or new_dy >= N or new_dy < 0:
                continue
            # 만약 보드의 다음 위치가 0이 아니거나 현재와 같지 않다면 계속 탐색
            if board[new_dx][new_dy] != 0 and board[new_dx][new_dy] != board[now_dx][now_dy]:
                remember_ps = []  # 돌을 계속 탐색하며 이동하면서 해당 돌의 정보를 담을 리스트 선언
                while True:
                    new_new_dx = new_dx + dx[i]  # 한번더 해당 방향으로 행 이동(새로운*2 돌이라고 칭함) 즉, 1칸 떨어져있는 돌위치
                    new_new_dy = new_dy + dy[i]  # 한번더 해당 방향으로 열 이동(새로운*2 돌이라고 칭함) 즉, 1칸 떨어져있는 돌위치

                    if 0 <= new_new_dx < N and 0 <= new_new_dy < N:  # 만약 해당 인덱스가 범위를 벗어나지 않는다면
                        if board[new_new_dx][new_new_dy] == 0:  # 만약 해당 보드판에 돌이 없다면
                            remember_ps = []  # 탐색했던 정보들은 의미가 없으므로 초기화 해주고
                            break  # 탈출
                        elif board[new_new_dx][new_new_dy] != board[now_dx][now_dy]:  # 만약 (새로운*2 돌) 위치와 현재 위치의 돌이 다르다면
                            remember_ps.append([new_dx, new_dy, board[now_dx][now_dy]])  # 중간에 낀 (새로운 돌*1) 위치의 정보를 리스트에 담는다.
                        elif board[new_new_dx][new_new_dy] == board[now_dx][now_dy]:  # 만약 (새로운*2돌)위치와 현재위치가 같다면
                            remember_ps.append([new_dx, new_dy, board[now_dx][now_dy]])  # (새로운 돌*1)위치의 정보를 리스트에 담는다.
                            break  # 만약 같다면 더이상 탐색할 필요가 없이 탐색했던 정보들을 토대로 돌을 바꿔주기 위해 탈출
                    else:  # 만약 인덱스를 벗어난다면
                        remember_ps = []  # 담았던 정보가 의미가 없으므로 빈 배열로 초기화 해주고
                        break  # 탈출
                    new_dx = new_new_dx  # (새로운*1) 위치를 (새로운*2위치)로 바꿔준다.(계속해서 같은 방향으로 이동하기 위해)
                    new_dy = new_new_dy  # (새로운*1) 위치를 (새로운*2위치)로 바꿔준다.(계속해서 같은 방향으로 이동하기 위해)

                if remember_ps:  # 만약 담았던 정보가 존재한다면
                    for a in remember_ps:  # 그 정보를 돌면서
                        board[a[0]][a[1]] = a[2]  # 그 정보로 보드판의 돌들을 바꿔준다.

    black, white = 0, 0
    for i in range(len(board)):
        black += board[i].count(1)
        white += board[i].count(2)

    print(f'#{order} {black} {white}')
