class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a hashmap with lexographically sorted strings as key
        # value will be index in our results list
        results = []
        hashmap = {}

        for s in strs: 
            key = "".join(sorted(s))
            if key in hashmap:
                results[hashmap[key]].append(s)
            else:
                hashmap[key] = len(results)
                results.append([s])
        
        return results 