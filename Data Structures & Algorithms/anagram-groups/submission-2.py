from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a hashmap with lexographically sorted strings as key
        # value will be index in our results list
        hashmap = defaultdict(list)

        for s in strs: 
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hashmap[tuple(count)].append(s)
        return list(hashmap.values()) 