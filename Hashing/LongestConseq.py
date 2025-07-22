class Solution:
    
    # Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self, arr):
        if not arr:
            return 0
        
        arr.sort()
        max_count = 1
        curr_count = 1
        
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1] + 1:
                curr_count += 1
                max_count = max(max_count, curr_count)
            elif arr[i] != arr[i-1]:  # skip duplicates
                curr_count = 1  # reset if not consecutive
        
        return max_count
