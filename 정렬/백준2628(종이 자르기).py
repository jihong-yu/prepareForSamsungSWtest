width, height = map(int, input().split())
N = int(input())
info_width = [0, width]  # 가로 길이를 구하기위해 점들을 저장할 리스트
info_height = [0, height]  # 세로 길이를 구하기 위해 점들을 저장할 리스트
for i in range(N):  # 입력 받은 개수 만큼 반복문 돈다.
    temp = list(map(int, input().split()))

    if temp[0] == 0:  # 만약 가로점을 입력받았다면
        info_height.append(temp[1])  # 세로 길이 리스트에 값들을 저장해준다.
    else:  # 만약 세로 점을 입력받았다면
        info_width.append(temp[1])  # 가로 길이 리스트에 세로길이들을 저장해준다.

info_width.sort()  # 오름차순 정렬
info_height.sort()  # 오름차순 정렬

width_list = []  # 전체 길이에서 잘라진 가로 길이들을 담을 리스트 선언
height_list = []  # 전체 길이에서 잘라진 세로 길이들을 담을 리스트 선언

# 각각의 나눠진 가로 길이 계산
for i in range(len(info_width) - 1):
    width_list.append(info_width[i + 1] - info_width[i])

# 각각의 나눠진 가로 세로 계산
for i in range(len(info_height) - 1):
    height_list.append(info_height[i + 1] - info_height[i])


# 각각 가장 긴 세로,가로 길이를 곱해준다.
print(max(height_list) * max(width_list))
