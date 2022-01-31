t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    new_b = b % 4  # 모든 제곱은 4번의 순환을 가짐.
    if new_b == 0:  # 만약 4번째라면(1,2,3은 그대로 값이 저장되나 4는 0으로 저장됨)
        new_b = 4  # 그 값을 4로 바꿔준다.
    number = a ** new_b
    if number % 10 == 0:  # 계산한 값의 일의자리가 0이라면
        print(10)  # 10을 출력
    else:  # 1~9 사이라면
        print(number % 10) #1~9 출력
