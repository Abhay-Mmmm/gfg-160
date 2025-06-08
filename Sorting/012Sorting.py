class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        n=len(arr)
        zero = []
        one = []
        two = []
        
        for i in range(n):
            if arr[i] == 0:
                zero.append(arr[i])
            elif arr[i] == 1:
                one.append(arr[i])
            else:
                two.append(arr[i])
                
        arr[:] = zero + one + two # [:] just clears the whole array.
        return arr