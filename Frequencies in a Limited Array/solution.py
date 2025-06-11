from collections import Counter

class Solution:
    def frequencyCount(self, arr):
        N = len(arr)
        count = Counter(arr)
        result = []
        for i in range(1, N + 1):
            result.append(count[i])
        return result
