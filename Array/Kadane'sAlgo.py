class Solution:
    def maxSubArraySum(self, arr):
        n = len(arr)
        
        currsum = arr[0]
        res = arr[0]
        for i in range(1,n):
            currsum = max(arr[i],arr[i]+currsum)
            res = max(res,currsum)
        return res
        
    #This is basically Kadane's Algorithm