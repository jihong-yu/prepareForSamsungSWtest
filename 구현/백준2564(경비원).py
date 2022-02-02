width, height = map(int, input().split())
N = int(input())
location = []  # c,r 좌표

for i in range(N + 1):
    direct, loc = map(int, input().split())
    if direct == 1:  # 북
        location.append([loc, height])
    elif direct == 2:  # 남
        location.append([loc, 0])
    elif direct == 3:  # 서
        location.append([0, height - loc])
    elif direct == 4:  # 동
        location.append([width, height - loc])

c_l = location.pop()  # 동근이의 현재위치를 리스트에서 빼서 저장
result = 0
for i in location:
    if c_l[1] == height or c_l[1] == 0:  # 서있는 위치가 위 혹은 아래일때
        if i[1] == height or i[1] == 0:  # 상점이 남 혹은 북에 있을때
            if i[1] == c_l[1]:  # 만약 같은 라인이라면
                result += abs(i[0] - c_l[0])
            elif i[1] != c_l[1]:  # 반대편 라인이라면
                result += min(c_l[0] + height + i[0], width - c_l[0] + height + width - i[0])
        elif i[0] == 0 or i[0] == width:  # 상점이 서 동에 있을때
            if c_l[1] == height:  # 동근이 위치가 꼭대기 일때
                if i[0] == 0:  # 만약 상점이 서쪽이라면
                    result += height - i[1] + c_l[0]
                elif i[0] == width:  # 상점이 동쪽이라면
                    result += width - c_l[0] + height - i[1]
            elif c_l[1] == 0:  # 동근이 위치가 맨아래일때
                if i[0] == 0:  # 만약 상점이 서쪽이라면
                    result += c_l[0] + i[1]
                elif i[0] == width:  # 상점이 동쪽이라면
                    result += i[1] + width - c_l[0]

    elif c_l[0] == 0 or c_l[0] == width:  # 서있는 위치가 동 혹은 서 일때
        if i[0] == 0 or i[0] == width:  # 상점이 동 혹은 서에 있을때
            if i[0] == c_l[0]:  # 만약 같은 라인이라면
                result += abs(i[1] - c_l[1])
            elif i[0] != c_l[0]:  # 만약 반대편 라인이라면
                result += min(c_l[1] + width + i[1], height - c_l[1] + width + height - i[1])
        elif i[1] == 0 or i[1] == height:  # 상점이 남 북에 있다면
            if c_l[0] == 0:  # 동근이 위치가 서쪽이라면
                if i[1] == height:  # 상점이 북쪽에 있다면
                    result += height - c_l[1] + i[0]
                elif i[1] == 0:  # 상점이 남쪽에 있다면
                    result += c_l[1] + i[0]
            elif c_l[0] == width:  # 동근이 위치가 동쪽이라면
                if i[1] == height:  # 상점이 북쪽에 있다면
                    result += height - c_l[1] + width - i[0]
                elif i[1] == 0:  # 상점이 남쪽에 있다면
                    result += c_l[1] + width - i[0]

print(result)