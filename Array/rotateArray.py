class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        temp = [-1] * n
        idx = 0
        d = d%n #For solving the problem occuring when d>n
        
        for i in range(d,n):
            temp[idx] = arr[i]
            idx += 1
            
        for j in range(0,d):
            temp[idx] = arr[j]
            idx += 1
            
        for k in range(0,n):
            arr[k] = temp[k]
            
        return arr