#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        seen = set(a)
        for i in range(len(b)):
            if b[i] not in seen:
                return False
        counter_a = Counter(a)
        counter_b = Counter(b)
        for i in range(len(b)):
            if counter_b[b[i]] > counter_a[b[i]]:
                return False
        return True
    
    
    
    
