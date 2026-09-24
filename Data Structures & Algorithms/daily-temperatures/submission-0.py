class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # tuple (temp, index)
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]: 
                index = stack.pop()[1]
                result[index] = (i - index)
            stack.append((temperatures[i], i))
        return result

