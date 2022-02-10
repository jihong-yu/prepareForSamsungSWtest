T = int(input())
word_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
a_dict = {}

for i in range(len(word_num)):
    a_dict[word_num[i]] = i
for order in range(1, T + 1):
    order2, N = input().split()
    N = int(N)
    array = list(input().split())

    new_array = []
    for i in range(N):
        new_array.append(a_dict.get(array[i]))

    new_array.sort()
    print(f'{order2} ')

    for i in range(len(new_array)):
        print(word_num[new_array[i]], end=" ")
    print()
