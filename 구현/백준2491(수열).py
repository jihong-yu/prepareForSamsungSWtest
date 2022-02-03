from collections import deque

N = int(input())
array = list(map(int, input().split()))

length1 = 0  # 큰 연속 수열 길이를 저장할 변수
length2 = 0  # 작은 연속 수열 길이를 저장할 변수
queue1 = deque()  # 큰 연속 수열을 찾기 위한 큐
queue2 = deque()  # 작은 연속 수열을 찾기 위한 큐

for i in range(N):
    # 큰 연속 수열 찾을 때
    if not queue1:  # 큐가 비어 있다면
        queue1.append(array[i])
    else:  # 큐가 비어있지 않다면
        if queue1[-1] <= array[i]:  # 만약 큐의 맨마지막 수보다 다음 들어올 수가 같거나 크다면
            queue1.append(array[i])  # 그 수를 큐에 추가
        else:  # 다음에 들어올 수가 현재 큐맨마지막 수보다 작다면
            if length1 < len(queue1):  # 만약 현재 길이가 저장된 길이보다 길다면
                length1 = len(queue1)  # 최대 길이를 저장된 길이로 바꿔주고
            queue1 = deque()  # 큐를 다시 초기화 해주고
            queue1.append(array[i])  # 그 다음 수부터 다시 시작하기위해 그 수를 넣어준다.

    # 작은 연속 수열 찾을 때
    if not queue2:  # 큐가 비어 있다면
        queue2.append(array[i])
    else:  # 큐가 비어있지 않다면
        if queue2[-1] >= array[i]:  # 만약 큐의 맨마지막 수보다 다음 들어올 수가 같거나 작다면
            queue2.append(array[i])  # 큐에 다음 수를 넣어준다.
        else:  # 다음에 들어올 수가 현재 큐맨마지막 수보다 크다면
            if length2 < len(queue2):  # 만약 현재 저장된 최대 길이보다 현재 큐에있는 길이가 길다면
                length2 = len(queue2)  # 그 길이를 최대 길이로 저장해준다.
            queue2 = deque()  # 다시 큐를 초기화하고
            queue2.append(array[i])  # 새로운 수부터 연속수열을 찾기위해 그 다음 값을 넣어준다.

    if i == N - 1:  # 만약 마지막 까지 돌았다면
        max_length_queue = max(len(queue1), len(queue2))  # 각각 수열의 길이중 긴것을 저장해준다.
        max_length = max(length1, length2)  # 만약 마지막 인덱스까지 길이가 저장되지 않았다면 현재 큐에 담겨있는 길이중 긴것을 저장해준다.
        print(max(max_length, max_length_queue))  # 저장된것중 큰것을 출력한다.
