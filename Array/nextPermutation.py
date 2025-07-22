#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        k = -1
        
        for i in range(0,n-1):
            if arr[i] < arr[i+1]:
                k = i
                
        if k == -1: # Reverse the whole array if there are no arr[i] < arr[i+1] (largest permutation reached)
            for i in range(n//2): 
                arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
            return arr
                
                
        for j in range(n-1,k,-1): # Swap the i and k elements
            if arr[k] < arr[j]:
                arr[k],arr[j] = arr[j],arr[k]
                break
        
        left,right = k+1,n-1 # To just reverse the sub-Array
        while left<right:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
            
        return arr