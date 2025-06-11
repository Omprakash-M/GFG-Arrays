from collections import Counter

class Solution:
    # Function to check if a is a subset of b
    def isSubset(self, a, b):
        count_a = Counter(a)
        flag = False
        for x in b:
            if count_a[x] <= 0:
                flag = False
                break
            else:
                count_a[x] -= 1
                flag = True
        return flag
