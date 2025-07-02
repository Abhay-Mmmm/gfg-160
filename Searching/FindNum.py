class Solution:
    def search(self,arr,key):
        if key not in arr:
            return -1
        
        for i in range (len(arr)):
            if arr[i] == key:
                return i