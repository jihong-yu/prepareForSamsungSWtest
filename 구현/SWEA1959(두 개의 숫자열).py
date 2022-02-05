def solution(Ai, Bj):
    result = []  # 곱의 합들을 저장할 리스트

    if len(Ai) > len(Bj):  # 만약 Ai의 길이가 Bj보다 더 길다면
        Ai, Bj = Bj, Ai  # 둘 리스트를 바꿔준다.

    start_j = 0  # 긴 길이를 가진 리스트 인덱스를 계산할 변수 선언 및 초기화
    while True:
        i = 0  # 짧은 길이를 가진 리스트 인덱스를 계산할 변수 선언 및 0 초기화
        j = start_j  # 긴 길이를 가진 리스트 인덱스를 start_j로 바꿔준다.
        temp = []  # 곱들을 저장할 임시 리스트
        while True:
            temp.append(Ai[i] * Bj[j])  # 같은 인덱스를 곱해준다.

            i += 1  # 길이가 더 짧은 리스트의 인덱스를 +1 씩해준다.
            j += 1  # 길이가 더 긴 리스트의 인덱스를 +1 씩해준다.

            if i == len(Ai):  # 만약 길이가 더 짧은 리스트의 인덱스가 끝에 도달했다면
                result.append(sum(temp))  # 곱들의 합을 추가해준다.
                start_j += 1  # 길이가 긴 인덱스는 그다음인덱스부터 비교해야 하므로 +1해주고
                break  # 반복문 탈출

        if len(result) == (len(Bj) - len(Ai) + 1):  # 만약 저장된 곱들의 합이 두리스트 길이의 차 + 1만큼 추가가 되었다면
            print(f'#{order} {max(result)}')  # 출력
            return


T = int(input())

for order in range(1, T + 1):
    N, M = map(int, (input().split()))
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    solution(Ai, Bj) #함수 실행
