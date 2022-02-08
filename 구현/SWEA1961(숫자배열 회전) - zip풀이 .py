def solution(order, array):
    result = []  # 회전시킨 행렬들을 담을 리스트
    temp_list_90 = list(map(list, zip(*array[::-1])))
    result.append(temp_list_90)
    temp_list2_180 = list(map(list, zip(*temp_list_90[::-1])))
    result.append(temp_list2_180)
    temp_list3_270 = list(map(list, zip(*temp_list2_180[::-1])))
    result.append(temp_list3_270)

    # 회전시킨 리스트들을 출력하기위해 열과 행을 바꾸어 준다.(전치)
    result = list(map(list, zip(*result)))

    print(f'#{order}')
    for i in result:
        for j in i:
            print("".join(map(str, j)), end=" ")
        print()


T = int(input())

for order in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    solution(order, array)
