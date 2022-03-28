def get_bowling_score(s):
    try_count_in_a_frame = 0
    frame = 1
    score = 0
    additional_array = [0] * (len(s) + 2)

    for i in range(len(s)):
        try_count_in_a_frame += 1
        if s[i] == 'S':
            add = 10
            if frame < 10:
                additional_array[i + 1] += 1
                additional_array[i + 2] += 1

        elif s[i] == 'P':
            if s[i - 1] == '-':
                add = 10
            else:
                add = 10 - int(s[i-1])
            if frame < 10:
                additional_array[i + 1] += 1
        else:

            if s[i] != '-':
                add = int(s[i])
            else:
                add = 0
        if s[i] == 'S' or try_count_in_a_frame == 2:
            try_count_in_a_frame = 0
            frame += 1
        score += add * (1 + additional_array[i])

    return score


assert get_bowling_score("9-8P72S9P-9S-P9-SS8") == 150
assert get_bowling_score("SSSSSSSSSSSS") == 300