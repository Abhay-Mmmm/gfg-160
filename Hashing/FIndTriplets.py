class Solution:
    def findTriplets(self, arr):
        index_map = {}
        result = set()

        for j in range(len(arr)):
            for k in range(j + 1, len(arr)):
                val = -1 * (arr[j] + arr[k])
                if val in index_map:
                    for i in index_map[val]:
                        if i < j:  # Ensure i < j < k
                            triplet = tuple(sorted([i, j, k]))
                            result.add(triplet)

            # Add j to the index map after it’s used
            if arr[j] not in index_map:
                index_map[arr[j]] = []
            index_map[arr[j]].append(j)

        return sorted([list(t) for t in result])
