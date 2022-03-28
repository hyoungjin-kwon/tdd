def get_bowling_score(s):
    frame = 1
    stack = 0
    answer = 0
    plus = []
    for i in range(len(s)):
        if s[i] == 'S':
            add = 10
            if frame < 10:
                plus.append(i + 1)
                plus.append(i + 2)
            stack = 0
            frame += 1
        else:
            stack += 1
            if stack == 2:
                stack = 0
                frame += 1
            if s[i] == 'P':
                if s[i - 1] == '-':
                    add = 10
                else:
                    add = 10 - int(s[i - 1])
                if frame < 10:
                    plus.append(i + 1)
            elif s[i] == '-':
                add = 0
            else:
                add = int(s[i])
        answer += add * (plus.count(i) + 1)

    return answer


assert get_bowling_score("9-8P72S9P-9S-P9-SS8") == 150
assert get_bowling_score("SSSSSSSSSSSS") == 300