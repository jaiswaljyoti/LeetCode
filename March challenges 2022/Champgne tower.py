class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if(poured==0):
            return 0.0
        l = [poured]
        for i in range(query_row):
            temp = [0]*(len(l)+1)
            for j in range(len(l)):
                pour = (l[j]-1)/2
                if(pour>0):
                    temp[j]+=pour
                    temp[j+1]+=pour
            l = temp
  
        return min(1, l[query_glass])