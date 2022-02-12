ret = []
TCs = int(input())
for T in range(1, TCs + 1):
    N, M, K = map(int, input().split())
    ppl = list(map(int, input().split()))
    ppl.sort()

    possible = True
    for i in range(N):
        if ppl[i] // M * K < i + 1:  # 해당 시간에 만들어진 붕어빵 보다 온 사람수가 더 많다면
            possible = False
            break

    ret.append(f'#{T} Possible\n' if possible else f'#{T} Impossible\n')

    print(''.join(ret))
