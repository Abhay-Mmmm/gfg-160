#User function Template for python3
from collections import defaultdict
class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        freq = defaultdict(int) #We use defaultdict(int) so that any key not found in the dictionary returns 0 by default.
        count = 0
        for num in arr:
            complement = target - num 
            count += freq[complement]
            freq[num] += 1
            
        return count