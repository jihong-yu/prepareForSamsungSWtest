for order in range(1, 10 + 1):
    dump_count = int(input())
    array = list(map(int, input().split()))

    for i in range(dump_count):
        max_ = max(array)  # 최댓값을 저장
        min_ = min(array)  # 최솟값을 저장
        array[array.index(max_)] = max_ - 1  # 최댓값의 인덱스에 최댓값 -1 을 저장해준다.
        array[array.index(min_)] = min_ + 1  # 최솟값의 인덱스에 최솟값 -1 을 저장해준다.

        new_max_ = max(array)  # 새로 계산된 최댓값을 찾는다.
        new_min_ = min(array)  # 새로 계산된 최솟값을 찾는다.

        if new_max_ - new_min_ < 2:  # 만약 그 값이 0 혹은 1 이라면
            break  # 반복문을 탈출한다.

    print(f'#{order} {new_max_ - new_min_}') #최댓값 - 최솟값을 출력
