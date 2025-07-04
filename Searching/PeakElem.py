class Solution:   
    def peakElement(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        if arr[0] > arr[1]:
            return 0

        for i in range(1, n - 1):
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                return i

        if arr[n - 2] < arr[n - 1]:
            return (n-1)

        return False