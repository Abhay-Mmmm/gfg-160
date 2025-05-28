class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self, arr):
        n = len(arr)
        maxprod = minprod = res = arr[0]
        for i in range(1, n):
            if arr[i] < 0:
                maxprod, minprod = minprod, maxprod

            maxprod = max(arr[i], arr[i] * maxprod)
            minprod = min(arr[i], arr[i] * minprod)
            res = max(maxprod, res)
        return res