from collections import defaultdict

class Solution:
    def anagrams(self, arr):
        anagram_map = defaultdict(list)

        for word in arr:
            key = ''.join(sorted(word))  # Sorted characters as the key
            anagram_map[key].append(word)

        return list(anagram_map.values())