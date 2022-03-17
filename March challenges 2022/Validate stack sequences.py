class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for char in pushed:
            if(char!=popped[i]):
                stack.append(char)
            else:
                i+=1
                while(len(stack)>0 and stack[-1]==popped[i]):
                    stack.pop()
                    i+=1
        if(i==len(pushed)):
            return True
        else:
            return False