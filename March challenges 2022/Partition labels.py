class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for idx, char in enumerate(s):
            lastIdx[char] = idx
            
        res = []
        startIdx = 0
        endIdx = -1

        for idx, char in enumerate(s):
            endIdx = max(lastIdx[char], endIdx)
            if idx == endIdx:
                res.append(endIdx - startIdx + 1)
                startIdx = endIdx + 1
        return res