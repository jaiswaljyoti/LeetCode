class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        while(k-n >= 26):
            ans.append(chr(122))
            n = n-1
            k = k-26
        else:
            while(n>1):
                ans.append(chr(97))
                n = n-1
                k = k-1
            else:
                ans.append(chr(97+k-1))
        ans.sort()
        return "".join(ans)