class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = {5: 0, 10: 0, 20: 0}

        for bill in bills: 
            if bill == 5: 
                hashmap[5] += 1
            elif bill == 10:
                if hashmap[5] > 0:
                    hashmap[5] -= 1
                    hashmap[10] += 1
                else:
                    return False
            else: 
                if hashmap[10] > 0 and hashmap[5] > 0: 
                    hashmap[10] -= 1
                    hashmap[5] -= 1
                    hashmap[20] += 1
                elif hashmap[5] > 2:
                    hashmap[5] -= 3 
                    hashmap[20] += 1
                else:
                    return False 
        return True 
                