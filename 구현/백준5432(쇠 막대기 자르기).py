import sys

sys.stdin = open('input.txt', 'r', encoding='UTF-8')


def solution():
    global total_count

    current_count = 0
    for i in range(len(raiser)):
        if raiser[i] == '(':
            if raiser[i + 1] != ')':  # 레이저가 아닐때
                current_count += 1
                total_count += 1
            else:  # 레이저 일때
                total_count += current_count
        else:  # ')' 일때
            if raiser[i - 1] != '(':  # 레이저가 아닐떄
                current_count -= 1


T = int(input())
for order in range(1, T + 1):
    raiser = input()

    total_count = 0

    solution()

    print(f'#{order} {total_count}')
