import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for order in range(1, T + 1):
    array = []

    length = 0  # 최대 길이 저장
    for i in range(5):
        temp = list(input())  # 입력 텍스트 저장
        array.append(temp)  # 입력 테스트를 배열에 추가
        if length < len(temp):  # 최대 길이를 저장
            length = len(temp)

    for i in array:  # 입력받은 텍스트를 돌면서
        while True:
            if len(i) < length:  # 만약 최대 길이보다 짧다면 빈문자열 추가
                i.append('')
            else:  # 길이가 같다면
                break  # 탈출

    new_word = ''
    for i in range(length):
        for j in range(5):
            new_word += array[j][i]

    print(f'#{order} {new_word}')
