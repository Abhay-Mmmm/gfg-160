class Solution:
    def inversionCount(self, arr):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, inv_left = merge_sort(arr[:mid])
            right, inv_right = merge_sort(arr[mid:])
            merged, inv_merge = merge(left, right)
            return merged, inv_left + inv_right + inv_merge

        def merge(left, right):
            merged = []
            i = j = inv_count = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    inv_count += len(left) - i  # All remaining elements in left > right[j]
                    j += 1
            merged += left[i:]
            merged += right[j:]
            return merged, inv_count

        _, count = merge_sort(arr)
        return count
