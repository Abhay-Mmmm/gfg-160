class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        temp = []
        freq = {}
        
        for num in arr:
            freq[num] = freq.get(num,0)+1
        # freq.get(num, 0) tries to get the current count of num in the dictionary.
        # If num is already in freq, it returns its count.
        # If num is not in freq, it returns 0 (the default).
        # Then, it adds 1 to that value and stores it back in freq[num].
        
        for i in range(n):
            count = 0
            
            if arr[i] in temp:
                continue
            
            if freq[arr[i]] > n//3:
                temp.append(arr[i])
        
        temp.sort()
    
        return temp