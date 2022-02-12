import sys

sys.stdin = open('input.txt', 'r')


def solution():
    rest_people = N  # 남은 사람수 저장
    current_amount = 0  # 현재 양을 저장
    for i in range(max(arrival) + 1):  # 도착하는 사람의 최대 시간까지 돈다.
        if i != 0 and i % M == 0:  # 만약 현재 시간이 0초가 아니면서 M초마다
            current_amount += K  # K를 만들어 낸다.
        if i in arrival:  # 만약 현재 시간에 도착하는 사람이 있다면
            current_count = arrival.count(i)  # 해당 시간에 도착한 사람수 계산
            rest_people -= current_count  # 남은 사람수를 계산하기위해 해당 시간에 도착한 사람수를 빼준다.
            current_amount -= current_count  # 그 사람 수 만큼 빼준다.
            if current_amount < 0:  # 만약 뺀 값이 음수라면
                print(f'#{order} Impossible')  # 붕어빵을 팔 수 없음을 출력
                return
            if current_amount >= rest_people:  # 만약 현재 양이 남은 사람보다 더많다면
                print(f'#{order} Possible')
                return


T = int(input())

for order in range(1, T + 1):
    # 사람수,만드는데 걸리는 시간,만들 수 있는 양
    N, M, K = map(int, input().split())
    arrival = list(map(int, input().split()))

    solution()  # 함수 실행
