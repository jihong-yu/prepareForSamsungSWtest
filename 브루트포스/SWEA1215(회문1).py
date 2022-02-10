# 회문 판별 함수
def palindrome_cheking(new_array):
    global count

    start = 0  # 시작 인덱스
    end = K - 1  # 끝 인덱스
    ispalindrome = True  # 회문판별여부 변수
    while start <= K // 2:  # 뽑은 길이의 절반만큼 양쪽에서 안쪽으로 검사

        if new_array[start] != new_array[end]:  # 만약 같지 않다면
            ispalindrome = False  # 그 값을 False
            break  # 반복문 탈출

        start += 1  # 앞에서오는 인덱스 + 1
        end -= 1  # 뒤에서 오는 인덱스 - 1

    if ispalindrome:  # 만약 회문이라면
        count += 1  # 총 개수 + 1


for order in range(1, 10 + 1):
    K = int(input())
    word = [list(map(str, input())) for _ in range(8)]

    count = 0
    # 가로 검사
    for i in range(8):
        for j in range(8):
            new_array = []
            if j + K > 8:  # 만약 K를 뽑을 수 없다면
                break  # 반복문 탈출후 다음 행으로 넘어간다.
            for h in range(j, j + K):  # 가로로 K를 뽑는다.
                new_array.append(word[i][h])  # 가로로 단어 k개를 넣어준다.

            palindrome_cheking(new_array)  # 회문 판별

    # 세로 검사
    for i in range(8):
        if i + K > 8:  # 만약 K를 뽑을 수 없다면
            break  # 반복문 탈출
        for j in range(8):
            new_array = []

            for h in range(i, i + K):  # 세로로 K개를 뽑는다.
                new_array.append(word[h][j])  # 세로로 단어 K개를 넣어준다.

            palindrome_cheking(new_array)  # 회문판별

    print(f'#{order} {count}')
