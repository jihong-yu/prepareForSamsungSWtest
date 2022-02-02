N = int(input())
temp = [0] * N
sequence = list(map(int, input().split()))
for i in range(1, N + 1):  # 1부터 ~ 5 번 학생을 줄을 세운다.
    # 번호를 받은 학생이 들어갈 자리 뒤에부터 끝까지의 학생들을 자리 뒤로 모두 그대로 옮겨준다.
    temp[i - sequence[i - 1]:] = temp[i - sequence[i - 1] - 1:-1]
    temp[i - sequence[i - 1] - 1] = i  # 그 후 빈자리에 해당 학생을 집어넣는다.

print(*temp)  # 언패킹 연산자로 간편하게 공백을 기준으로 출력
