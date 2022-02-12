def solution(new_id=''):
    #1
    temp1 = ''
    special_word = ['-', '_', '.']
    for i in new_id.lower():
        if i in special_word or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
            temp1 += i
    #2
    temp2 = ''
    for i in range(len(temp1)):
        if i == len(temp1) - 1:
            temp2 += temp1[i]
            break
        if temp1[i] == '.' and temp1[i + 1] == '.':
            continue
        temp2 += temp1[i]
    #3
    temp3 = temp2.strip('.')

    #4
    temp4 = ''
    if len(temp3) == 0:
        temp4 += 'a'
    else:
        temp4 = temp3

    #5
    temp5 = ''
    if len(temp4) >= 16:
        for i in range(15):
            temp5 += temp4[i]
    else:
        temp5 = temp4

    #6
    temp6 = temp5.rstrip('.')

    #7
    temp7 = temp6
    last_word = temp6[-1]
    if len(temp6) <= 2:
        while True:
            temp7 += last_word

            if len(temp7) >= 3:
                break
    answer = temp7

    return answer

