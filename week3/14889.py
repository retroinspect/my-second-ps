# 스타트와 링크
N = int(input())
S = []
for i in range(N):
    line = list(map(int, input().split(' ')))
    S.append(line)

def getScoreDiff(startMembers, S):
    startScore = 0
    for i in startMembers:
        for j in startMembers:
            startScore += S[i][j]

    linkScore = 0
    for i in range(N):
        if i in startMembers:
            continue
        for j in range(N):
            if j in startMembers:
                continue
            linkScore += S[i][j]

    return abs(startScore - linkScore)

def getMinScoreDiff(startMembers, idx, S):
    if len(startMembers) == N//2:
        return getScoreDiff(startMembers, S)
    
    if N//2 - len(startMembers) == N - idx:
        return getScoreDiff(startMembers + list(range(idx, N)), S)

    scoreWithoutIdx = getMinScoreDiff(startMembers, idx+1, S)
    scoreWithIdx = getMinScoreDiff(startMembers + [idx], idx+1, S)
    
    return min(scoreWithoutIdx, scoreWithIdx)

answer = getMinScoreDiff([], 0, S)
print(answer)