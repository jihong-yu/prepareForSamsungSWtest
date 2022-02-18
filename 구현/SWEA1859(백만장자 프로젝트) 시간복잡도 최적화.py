import sys

sys.stdin = open('input.txt', 'r')


def solution():
    profit = 0

    max_ = cost[-1]
    for i in range(-2, -(1 + N), -1):
        if max_ < cost[i]:
            max_ = cost[i]
        else:
            profit += (max_ - cost[i])
    return profit


T = int(input())

for order in range(1, 1 + T):
    N = int(input())
    cost = list(map(int, input().split()))

    print(f'#{order} {solution()} ')