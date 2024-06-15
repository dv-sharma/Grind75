from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early return if the lengths of the strings are not equal
        if len(s) != len(t):
            return False
        
        # Use Counter to count characters in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Compare the two Counter objects
        return count_s == count_t

# Test case
s = "aacc"
t = "ccac"
sol = Solution()
print(sol.isAnagram(s, t))  # Output should be False
