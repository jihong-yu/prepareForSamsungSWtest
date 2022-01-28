N, K = map(int, input().split())

list_ = list(map(int, input().split()))

i = 0  # 초기 시작 변수
j = K  # K -1 인덱스까지의 합을 초기에 구하기 위해 지정하는 변수.

max_result = sum(list_[i:j])  # 초기 0~k-1 까지의 합을 구한다.
a = max_result  # 초기 합의 값을 a라는 변수에 저장
while True:  # 반복문을 돈다.
    if j == N:  # 만약 j가 끝 인덱스라면 탈출
        break

    # 임시변수에 현재 저장된 최대값 - 기존의 맨앞의 값 + 기존의 맨뒤의 인덱스 + 1에 존재하는 값
    temp = a - list_[i] + list_[j]

    if max_result < temp:  # 만약 새로운 수열의 합이 기존의 최댓값보다 크다면
        max_result = temp  # 그 값을 최대값으로 수정

    i += 1  # 맨 앞 인덱스 i를 +1 해준다.
    j += 1  # 맨 뒤 인덱스 j를 +1 해준다.
    a = temp  # 새로 계산된 값을 a 라는 변수에 다시 넣어준다.

print(max_result)