class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        res = 1
        places = 2*n
        for _ in range(n):
            res *= (places*(places-1))//2
            res %= MOD
            places = places-2
            
        return res