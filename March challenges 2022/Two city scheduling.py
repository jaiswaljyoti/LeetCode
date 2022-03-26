class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        totalA = 0
        for costA, _ in costs:
            totalA += costA
            
        difference = []
        for costA, costB in costs:
            difference.append(costB-costA)
        
        totalB = sum(sorted(difference)[:len(costs)//2])
		
        return totalA + totalB