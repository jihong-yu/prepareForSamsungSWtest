import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

for order in range(1, 10 + 1):
    V, E = map(int, input().split())
    array = list(map(int, input().split()))
    indegree = [0] * (V + 1)  # 들어오는 차수 저장
    graph = [[] for _ in range(V + 1)]
    for i in range(0, E * 2, 2):
        a, b = array[i], array[i + 1]  # 연결된 그래프 조사
        graph[a].append(b)  # a -> b 간선 저장
        indegree[b] += 1  # b에 들어오는 차수 1개 추가

    queue = deque()  # 그래프 이동을 검사할 큐
    result = []  # 간선을 따라 이동한 결과를 출력할 리스트

    # 우선 차수가 0인 노드들을 큐에 추가해준다.
    for i in range(1, V + 1):
        if not indegree[i]:
            queue.append(i)
    while queue:  # 큐가 빌때까지 돈다.

        start = queue.popleft()  # 시작 노드를 꺼낸다.
        result.append(start)  # 그 꺼낸 노드를 결과리스트에 추가해주고

        for i in graph[start]:  # 그 노드와 연결된 노드들을 탐색한다.
            indegree[i] -= 1  # 한번 탐색을 했기 때문에 들어오는 간선 한개를 빼준다.

            if not indegree[i]:  # 만약 해당 노드에 들어오는 간선이 없다면
                queue.append(i)  # 그 노드를 큐에 추가해준다.

    print(f'#{order} {" ".join(map(str, result))}')
