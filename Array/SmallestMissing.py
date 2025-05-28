class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        arr.sort()
        temp = [x for x in arr if x > 0]
        m = len(temp)
        
        if not temp or temp[0] != 1:
            return 1
        
        for i in range(m-1):
            if temp[i+1]-temp[i] > 1:
                return temp[i] + 1
        
        return temp[-1] + 1