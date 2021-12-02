class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[int]:

        lst  = sorted(score, reverse=True)
        glod = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        d = {}
        count = 3
        
        for i in range(len(score)):
            if count:
                d[lst[i]] = glod[i]
                count -= 1
            else:
                d[lst[i]] = str(i + 1)

        for i in range(len(score)):
            score[i] = d[score[i]]
        return score
