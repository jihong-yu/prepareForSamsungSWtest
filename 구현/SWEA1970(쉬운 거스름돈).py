T = int(input())
cost = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in range(T):
    N = int(input())
    result = []  # 각 금액의 개수를 저장할 리스트
    for j in cost:  # 5만원부터 계산을 한다.
        result.append(N // j)  # 각 금액의 필요 최솟값을 몫으로 구해준다.
        N = N % j  # 그 후 남은 금액을 N으로 바꿔준다.
    print(f'#{i + 1}')
    print(*result)
