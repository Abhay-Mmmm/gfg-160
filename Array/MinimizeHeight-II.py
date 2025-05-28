class Solution:
    def getMinDiff(self, arr,k):
        arr.sort()
        n=len(arr)
        if n == 1:
            return 0
        
        ans = arr[-1] - arr[0]
        
        for i in range(1,n):
            if arr[i] < k:
                continue
            
            min_value = min(arr[0]+k,arr[i]-k)
            max_value = max(arr[-1]-k,arr[i-1]+k)
            ans = min(ans,max_value - min_value)
        
        return ans