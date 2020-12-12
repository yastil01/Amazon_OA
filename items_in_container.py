def countItems(s, startIndices, endIndices):
    totalStars = []
    for start, end in zip(startIndices, endIndices):
        seenVerticalBar = 0
        countStars = 0
        tempCountStars = 0
        for c in s[start-1:end]:
            if c == '*':
                tempCountStars += 1
            elif c == '|':
                seenVerticalBar += 1
                if seenVerticalBar == 2:
                    countStars += tempCountStars
                    seenVerticalBar = 1
                    tempCountStars = 0
                elif seenVerticalBar == 1:
                    tempCountStars = 0
        
        print(s[start-1:end], countStars)

        totalStars.append(countStars)

    return totalStars
