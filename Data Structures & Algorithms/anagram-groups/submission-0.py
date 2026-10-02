class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort strings to get lexographical representations
        # create hashmap which cooresponds to where in the resulting list the representation is
        # append to result

        result = []
        hashmap = {}

        for string in strs: 
            canonical = "".join(sorted(string))

            if canonical in hashmap: 
                result[hashmap[canonical]].append(string)
            else: 
                hashmap[canonical] = len(result)
                result.append([string])
        return result