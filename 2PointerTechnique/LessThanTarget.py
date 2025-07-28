class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        n = len(arr)
        arr.sort()
        count = 0
        i = 0
        j = n-1
        while i < j:
            if arr[i] + arr[j] < target:
                count += (j - i)
                i += 1
            else:
                j -= 1
        return count