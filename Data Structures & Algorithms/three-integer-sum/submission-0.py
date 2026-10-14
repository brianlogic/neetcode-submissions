class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O (n ^ 2) 

        # idea: we perform 2 sum on the previous elements with the target being the negative of our current number:

        # elements not guaranteed to be unique so hashmap won't work

        # we cannot create duplicates, so let's use a tuple and check for membership in a set

        result = []
        hashmap = {} 
        for i in range(len(nums)):
            target = -nums[i]
            for j in range(i): 
                if (target - nums[j]) in hashmap and hashmap[target - nums[j]] != j: 
                    solution = sorted((target - nums[j], nums[j], nums[i]))
                    if not solution in result:
                        result.append(solution)
            if not nums[i] in hashmap: 
                hashmap[nums[i]] = i 
        
        return result 