class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        count = 0

        for i in range(n):
            seen = {}
            for j in range(i + 1, n):
                complement = target - arr[i] - arr[j]
                if complement in seen:
                    count += seen[complement]
                seen[arr[j]] = seen.get(arr[j], 0) + 1

        return count