class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        res = [1]*n
        
        prefix = 1
        for i in range(n): # To get the product for elements in front of the element
            res[i] = prefix
            prefix *= arr[i]

        suffix = 1
        for j in range(n-1,-1,-1): # To get the product for elements behind of the element
            res[j] *= suffix
            suffix *= arr[j]
        
        return res