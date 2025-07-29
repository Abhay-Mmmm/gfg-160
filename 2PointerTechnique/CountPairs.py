class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        count = 0
        seen = {}
        
        for num in arr:
            complement = target - num
            if complement in seen:
                count += seen[complement]
            seen[num] = seen.get(num,0) + 1
    
        return count