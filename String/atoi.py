class Solution:
    def myAtoi(self, s):
        arr = s.strip()
        sign = 1
        MIN = -2**31
        MAX = 2**31 - 1
        
        if arr[0] == "-":
            sign = -1
            arr = arr[1:]
        elif arr[0] == "+":
            arr = arr[1:]
        
        n = len(arr)
        i = 0
        num = 0
        while i<n and arr[i].isdigit():
            num = num*10 + int(arr[i])
        
            if sign == 1 and num > MAX:
                return MAX
            elif sign == -1 and -num < MIN:
                return MIN
            
            i += 1
        
        return (sign*num)