w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

r = q  # 초기 행값 저장
c = p  # 초기 열값 저장
count = 0  # 시간을 셀 변수
cycle_c = 1  # 열이 증가하는지 감소하는지 체킹변수
cycle_r = 1  # 행이 증가하는지 감소하는지 체킹 변수
while True:

    if r == h:  # 만약 행이 젤 끝인덱스라면
        cycle_r = -1  # 사이클을 반대로
    elif r == 0:  # 만약 행이 처음이라면
        cycle_r = 1  # 사이클을 반대로

    if cycle_r == 1:  # 만약 증가 사이클이라면
        r += 1  # 증가
    elif cycle_r == -1:  # 만약 감소사이클이라면
        r -= 1  # 감소

    if c == w:  # 만약 열이 젤 끝 인덱스라면
        cycle_c = -1  # 사이클을 반대로
    elif c == 0:  # 만약 열이 처음이라면
        cycle_c = 1  # 사이클을 반대로

    if cycle_c == 1:  # 만약 증가 사이클이라면
        c += 1  # 증가
    elif cycle_c == -1:  # 만약 감소사이클이라면
        c -= 1  # 감소

    count += 1  # 위에 실행이 한번 되었다면 시간 증가

    if count == t:  # 만약 시간이 입력받은 시간과 동일하다면
        print(c, r)  # 해당 열,행 출력
        break  # 반복문 탈출
