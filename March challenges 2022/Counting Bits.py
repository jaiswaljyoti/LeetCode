class Solution:
    def countBits(self, n: int) -> List[int]:
        l = [0]*(n+1)
        l[0] = 0
        for i in range(1, n+1):
            l[i] = 1+l[i-1 & i]
        
        return l