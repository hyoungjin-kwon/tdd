def get_bowling_score(s):
    count = 0
    frame = 1
    score = 0


    for i in range(len(s)):
        temp = []
        if s[i] == 'S':
            frame += 1
            score += 10
            count = 0

            if frame <= 11:
                temp.append(s[i + 1])
                temp.append(s[i + 2])

        elif s[i] == 'P':
            frame += 1
            if s[i-1] != '-':
                score += 10 - int(s[i-1])
            else:
                score += 10
            count = 0
            if frame <= 11:
                temp.append(s[i + 1])

        else:
            if count == 1:
                frame += 1
                count = 0
            else:
                count = 1
            if s[i] != '-':
                score += int(s[i])

       # print(temp)
      #  print('--')
        prev = 0
       # cnt = len(temp)
      #  print(frame, score, cnt)
        for j in range(len(temp)):
       #     print(temp[j])
            if frame <= 10:
                if temp[j] != '-':
                    if temp[j] == 'P':

                        score += 10 - prev
               #         print(score, str(frame) + str(prev) + 'dd')
                        prev = 0
                    elif temp[j] == 'S':
                        score += 10
           #            print(score)
                    else:
                        score += int(temp[j])
                        prev = int(temp[j])
          #              print(score, str(prev) + 'd')
           #         cnt -= 1
        """   if frame == 10:
               # temp.pop(0)
              #  print(temp)
                if temp[j+1] == 'S':
                    score += 10
                elif temp[j+1] == 'P':
                    if temp[j] != '-':
                        score += 10 - int(temp[j])
                else:
                    if temp[j+1] != '-':
                        score += int(temp[j+1])
                break"""
         #   temp.pop(0)
         #   print(temp)
         #   print('-')
         #   print(score, cnt)


         #   if frame == 10:
          #      if s[i+1] == 'S':
           # continue
    print(score)
    return score


assert get_bowling_score("9-8P72S9P-9S-P9-SS8") == 150
assert get_bowling_score("SSSSSSSSSSSS") == 300