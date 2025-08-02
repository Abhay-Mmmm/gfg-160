class Solution:
    def maxWater(self, arr):
        n = len(arr)
        left = 0 
        right = n-1
        max_area = 0
        while left < right:
            b = right - left
            l = min(arr[left],arr[right])
            if l*b > max_area:
                max_area = l*b
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return max_area