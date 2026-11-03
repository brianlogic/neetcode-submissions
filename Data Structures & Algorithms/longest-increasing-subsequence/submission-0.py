class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [] 
        for num in nums: 
            if not tails or num > tails[-1]:
                tails.append(num)
            else: # tails less than last element so we have to replace an element
                l = 0 
                r = len(tails)
                while l < r: 
                    mid = (l + r) // 2
                    if tails[mid] < num: 
                        l = mid + 1
                    else:
                        r = mid
                tails[l] = num 
        return len(tails)