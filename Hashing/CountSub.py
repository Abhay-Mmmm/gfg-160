class Solution:
    def cntSubarrays(self, arr, k):
        res = 0
        curr = 0 
        sums = {0:1}
        for num in arr:
            curr += num
            
            if curr - k in sums:
                res += sums[curr-k]
            
            sums[curr] = sums.get(curr,0) + 1
            
        return res