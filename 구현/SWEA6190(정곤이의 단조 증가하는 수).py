import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for order in range(1, T + 1):

    N = int(input())
    array = list(map(int, input().split()))
    result = -1  # Ai * Aj 의 최댓값을 출력할 변수 (없다면 그대로 -1 출력)
    for i in range(N):  # 2개를 뽑기 위해 우선 배열의 전체를 돈다.
        for j in range(i + 1, N):  # 위의 반복문에서 정해진 인덱스의 그 다음 인덱스부터 돈다.(중복해서 뽑지 않기 위해)
            num = array[i] * array[j]  # 뽑은 2개를 곱한다.

            danjo = True  # 단조의 여부를 우선 True 설정
            for k in range(len(str(num)) - 1):  # 곱해진 숫자를 문자열로 바꾼후 각 자리수를 검사한다.
                if int(str(num)[k]) > int(str(num)[k + 1]):  # 만약 각자리수 숫자 값이 다음 자릿수에 나오는 숫자보다 크다면
                    danjo = False  # 단조가 아니므로 단조 여부를 False 후 탈출
                    break
            if danjo:  # 만약 단조라면
                if result < num:  # 그 곱의 값이 저장된 곱의 값보다 크다면
                    result = num  # 그 값을 최댓값으로 설정

    print(f'#{order} {result}')
