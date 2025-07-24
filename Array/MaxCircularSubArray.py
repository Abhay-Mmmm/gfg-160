class Solution:
    def kadane(self, arr) -> int:
        size =  len(arr)
        
        max_kadane = curr_max = min_kadane = arr[0]
        
        #Kadane's Algorithm
        for i in range(1,size):
            max_kadane = max(arr[i],arr[i]+max_kadane)
            curr_max = max(max_kadane,curr_max)
        return curr_max
        
    def circularSubarraySum(self,arr) -> int:
        inverted = [-x for x in arr]
        kadane_min = self.kadane(inverted)
        kadane_max = self.kadane(arr)
        
        total_sum = sum(arr)
        wrap = total_sum + kadane_min
        
        if wrap == 0:
            return kadane_max
        else:
            return max(kadane_max,wrap)