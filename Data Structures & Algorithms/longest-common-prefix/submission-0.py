class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "" 
        
        first = strs[0]

        prefix = [] 

        for i in range(len(first)): 

            for j in range(1, len(strs)):
                if len(strs[j]) == i or first[i] != strs[j][i]:
                    return "".join(prefix)
            prefix.append(first[i])
        
        return "".join(prefix)