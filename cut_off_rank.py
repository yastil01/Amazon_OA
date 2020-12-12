def countLevelUpPlayers(cutOffRank, num, scores):                        
    count = [0] * 101 # for storing count of 0 to 100 scores
    for i in scores:
        count[i] += 1
    c = 0
    for i in count[::-1]:
        # Only if c >= cutoff, we should exit. Once we get into a score, we should take all count irrespective of cutoffrank.
        if c >= cutOffRank:
            break 
        c += i
    return c
